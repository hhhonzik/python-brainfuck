import zlib, struct;


class PNGWrongHeaderError(Exception):
    pass


class PNGNotImplementedError(Exception):
    pass


class PngReader():
    def __init__(self, filepath):
        self.rgb = []
        self.idat = bytearray()

        self.width = 0
        self.height = 0

        self.file = open(filepath, mode="rb");

        self.checkHeader().parse().process();

        self.file.close();

    def checkHeader(self):
        # is PNG ?
        if self.file.read(8) != b"\x89PNG\r\n\x1a\n":
            self.file.close();
            raise PNGWrongHeaderError("Loaded file is probably not a PNG image.")

        return self;

    def parse(self):

        while True:
            chunk = {x: '' for x in ['length', 'type', 'data', 'crc']}
            chunk['length'] = self.btoi(self.file.read(4));
            chunk['type'] = self.file.read(4);
            chunk['data'] = self.file.read(chunk['length']);
            chunk['crc'] = self.btoi(self.file.read(4));

            if chunk['type'] == b'IEND':
                break;
            else:
                #process chunk

                op = self.chunkoperation(chunk['type']);
                if op:
                    op(chunk);
                else:
                    self.file.close();
                    raise PNGNotImplementedError( "Chunk {0} not compatible. Data: {1}".format(chunk["type"], chunk) );
                    break;

                # print "Parse", chunk['type'];
                #(chunk);


                # >>chunk_length + 3*(size of int)
                # self.bytes = self.bytes[chunk['length'] + 12:]

        # dekomprese

        self.idat = zlib.decompress(bytes(self.idat));

        return self;

    def chunkoperation(self, type):
        return {
            b'IHDR': self.ihdr,
            b'IDAT': self.p_idat,
        }.get(type);

    def ihdr(self, chunk):
        self.width = self.btoi(chunk['data'][:4])
        self.height = self.btoi(chunk['data'][4:8])
        # z prednasek
        if chunk['data'][8:] != b'\x08\x02\x00\x00\x00':
            self.file.close();
            raise PNGNotImplementedError("Loaded image has a structure that cannot be processed.")





    def p_idat(self, chunk):
        # print(chunk['data']);
        self.idat += chunk['data'];

    def btoi(self, bytes):

        # python 2.x bytes
        try:
            bytes =  bytearray(bytes);

            r = bytes[0] << 24
            r += bytes[1] << 16
            r += bytes[2] << 8
            r += bytes[3]
        except:
            return 0;

        return r;


    def getPixel(self, b):
        v = b;
        if v == -1:
            v = 255;
        return (v + 256) % 256;

    def process(self):

        i = 0
        for row in range(0, self.height):
            line = []
            self.idat[i]
            pngfilter = self.idat[i];
            i += 1
            for col in range(0, self.width):
                pixel = (self.getPixel(self.idat[i]), self.getPixel(self.idat[i + 1]), self.getPixel(self.idat[i + 2]));
                i += 3

                # None filtr
                if pngfilter == 0:
                    a = pixel
                    line += [pixel]
                    # Up filtr
                elif pngfilter == 1:
                    if col == 0:
                        a = (0, 0, 0)
                        a = pixel
                    else:
                        a = ((pixel[0] + a[0] + 256)%256, (pixel[1] + a[1] + 256)%256, (pixel[2] + a[2] + 256)%256)

                    line += [a]
                elif pngfilter == 2:
                    if row == 0:
                        b = (0, 0, 0)
                        a = pixel
                    else:
                        b = self.rgb[row - 1][col]
                        a = ((pixel[0] + b[0]+ 256) % 256, (pixel[1] + b[1]+ 256) % 256, (pixel[2] + b[2]+ 256) % 256)

                    line += [a]

                # Average filtr
                elif pngfilter == 3:
                    if row == 0:
                        b = (0, 0, 0)
                    else:
                        b = self.rgb[row - 1][col]

                    if col == 0:
                        a = (0, 0, 0)
                    else:
                        a = line[col - 1]

                    pixel = ((pixel[0] + (a[0] + b[0]) // 2 + 256) % 256, (pixel[1] + (a[1] + b[1]) // 2 + 256) % 256,
                             (pixel[2] + (a[2] + b[2]) // 2 + 256) % 256)

                    line += [pixel]

                elif pngfilter == 4:
                    if row == 0 or col == 0:
                        c = (0, 0, 0)
                    else:
                        c = self.rgb[row - 1][col - 1]

                    if row == 0:
                        b = (0, 0, 0)
                    else:
                        b = self.rgb[row - 1][col]

                    if col == 0:
                        a = (0, 0, 0)
                    else:
                        a = line[col - 1]

                    pixR = (pixel[0] + self.paeth(a[0], b[0], c[0]) + 256) % 256
                    pixG = (pixel[1] + self.paeth(a[1], b[1], c[1]) + 256) % 256
                    pixB = (pixel[2] + self.paeth(a[2], b[2], c[2]) + 256) % 256
                    pixel = (pixR, pixG, pixB)

                    line += [pixel]
                else:
                    raise PNGNotImplementedError(
                        "Loaded image uses filter which is not supported: {0}".format(pngfilter))


            self.rgb += [line]

        return;


    def paeth(self, a, b, c):
        p = a + b - c
        pa = abs(p - a)
        pb = abs(p - b)
        pc = abs(p - c)

        if pa <= pb and pa <= pc:
            return a
        elif pb <= pc:
            return b
        else:
            return c


class PngWriter():
    def __init__(self, filepath, width, height, data):

        self.file = open(filepath, mode="wb");

        self.writeHeader(width,height).writeData(data).writeEnd();

        self.file.close();



    def writeHeader(self, width, height):
        # PNG header
        self.file.write(b'\x89PNG\r\n\x1a\n');
        # self.file.write(b'\x00'); # ???

        #IHDR chunk

        chunk = {x: '' for x in ['length', 'type', 'data', 'crc']}
        chunk['length'] = 13; # width (4) + height (4) + other (5);
        chunk['type'] = b'IHDR';
        chunk['data'] = self.itob(width) + self.itob(height) + b'\x08\x02\x00\x00\x00';


        self.write(chunk);

        return self;
    def itob(self, x, unsigned=True ):
        return x.to_bytes(4, 'big');

    def writeData(self, colors):
        chunk = {x: '' for x in ['length', 'type', 'data', 'crc']}
        chunk['type'] = b"IDAT";
        chunk['data'] = b'';
        i = 0;
        for line in colors:
            i+=1;

            chunk['data'] += struct.pack("B", 00);
            j = 0;
            for pixel in line:

                j+=1;
                chunk['data'] += struct.pack("B", pixel[0]);
                chunk['data'] += struct.pack("B", pixel[1]);
                chunk['data'] += struct.pack("B", pixel[2]);

        chunk['data'] = zlib.compress( chunk['data'] );
        chunk['length'] = len(chunk['data']);


        self.write(chunk);

        return self;

    def writeEnd(self):

        #end chunk
        self.file.write(self.itob(0) + b'IEND' + b'' + self.itob(zlib.crc32(b'IEND'), False))
        return self;

    def write(self, chunk):
        chunk['crc'] = zlib.crc32( bytes(chunk['type'])+chunk['data'] );

        self.file.write(self.itob(chunk['length'], False));
        self.file.write(chunk['type']);
        self.file.write(chunk['data']);
        self.file.write(self.itob(chunk['crc'], False))

