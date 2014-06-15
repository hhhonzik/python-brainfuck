# -*- coding: utf-8 -*-
import math, sys, types;
from interface import coderInterface;
from ..ImageParser import PngWriter;

class BrainLoller (coderInterface):
    """A class to process brainloller language."""

    def __init__(self, input, output):

        # data programu
        try:
            # je to soubor
            with open(input, mode="r") as _file:
                self.data = _file.read()
        except:
            # výjimka -> rovnou data
            self.data = input;

        # image size
        self.width = int(math.ceil(math.sqrt(len(self.data) ) ) +1 ); # arrows on end / start;

        data = self.code(self.data);

        self.output = "BrainFuck code Written to {0}".format(output);
        self.outputImg = PngWriter(output, self.width, self.height, data);


    def code(self, data):
        """Parsing Brainfuck code and write as PNG file."""
        colors = [];
        line = [];
        pushed = 0;
        self.height = 1;
        x = 0;

        op = 0;
        ended = False;
        while True:
            x += 1;
            if x == self.width:
                # end of the line, always go right
                x = 0;
                self.height += 1;

                if self.height % 2 == 1:
                    line.reverse();

                if self.height > 2:
                    line.reverse();
                    line.append((0,128,128));
                    line.reverse();

                line.append( (0,255,255) );

                colors.append(line);

                if ended:
                    self.height -= 1;
                    break;

                line = [];
            elif self.height > 1 and x == 1:
                # if not the first line, turn always left
                op = 0;
            else:

                if pushed == len(data):
                    # 100% last row
                    if self.height % 2 == 0:
                        line.append( (0,255,255) );
                    else:
                        line.append( (0,128,128) );
                    ended = True;
                else:
                    line.append( self.getcolor( data[ pushed ] ) );
                    pushed += 1;


        return colors;

    def getcolor(self, name):
        return {
             ">" : (255,0,0),
             "<" : (128,0,0),
             "+" : (0,255,0),
             "-" : (0,128,0),
             "." : (0,0,255),
             "," : (0,0,128),
             "[" : (255,255,0),
             "]" : (128,128,0)
        }.get(name);

    def render(self):
        print self.output;