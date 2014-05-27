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

    def checkHeader(self):
        # is PNG ?
        if self.file.read(8) != b"\x89PNG\r\n\x1a\n":
            raise PNGWrongHeaderError("Loaded file is probably not a PNG image.")

        return self;

    def parse(self):

        while True:
            chunk = {x: '' for x in ['length', 'type', 'data', 'crc']}
            chunk['length'] = ( self.btoi(self.file.read(4)) + 256) % 256;
            chunk['type'] = self.file.read(4);
            chunk['data'] = self.file.read(chunk['length']);
            chunk['crc'] = self.btoi(self.file.read(4));

            if chunk['type'] == 'IEND':
                break
            else:
                #process chunk

                op = self.chunkoperation(chunk['type']);
                if op:
                    op(chunk);

                # print "Parse", chunk['type'];
                #(chunk);


                # >>chunk_length + 3*(size of int)
                # self.bytes = self.bytes[chunk['length'] + 12:]

        # dekomprese

        self.idat = zlib.decompress(bytes(self.idat));

        return self;

    def chunkoperation(self, type):
        return {
            'IHDR': self.ihdr,
            'IDAT': self.p_idat,
        }.get(type);

    def ihdr(self, chunk):
        self.width = self.btoi(chunk['data'][:4])
        self.height = self.btoi(chunk['data'][4:8])
        # z prednasek
        if chunk['data'][8:] != b'\x08\x02\x00\x00\x00':
            raise PNGNotImplementedError("Loaded image has a structure that cannot be processed.")


    def p_idat(self, chunk):
        self.idat += bytes(chunk['data']);

    def btoi(self, bytes):

        # python 2.x bytes
        try:
            bytes =  bytearray(bytes);
        except:
            raise Exception;

        r = bytes[0] << 24
        r += bytes[1] << 16
        r += bytes[2] << 8
        r += bytes[3]
        return r;


    def getPixel(self, b):
        v = struct.unpack("b", b)[0];
        if v == -1:
            v = 255;
        return (v + 256) % 256;

    def process(self):
        i = 0
        for row in range(0, self.height):
            line = []
            pngfilter = struct.unpack("b", self.idat[i])[0];
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