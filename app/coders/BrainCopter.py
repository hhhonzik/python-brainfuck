# -*- coding: utf-8 -*-
import math, sys, types;
from interface import coderInterface;
from ..ImageParser import PngWriter, PngReader;

class IOException(Exception):
    pass

class BrainCopter (coderInterface):
    """A class to process brainloller language."""

    def __init__(self, input, output, source):
        # data programu
        try:
            # je to soubor
            with open(input, mode="r") as _file:
                self.data = _file.read()
        except:
            # výjimka -> rovnou data
            self.data = input;

        # data vstupu
        try:
            with open(input, mode="r") as _file:
                self.data = _file.read()
        except:
            raise IOException("Input file does not exists");

        self.source = PngReader(source)



        self.width = self.source.width; # image size

        data = self.code(self.data, self.source);

        self.outputImg = PngWriter(output, self.source.width, self.source.height, data);

        self.output = "BrainFuck code Written to {0}".format(output);


    def code(self, data, source):
        """Parsing Brainfuck code and write as PNG file."""
        colors = [];
        line = [];
        pushed = 0;
        x = 0;

        op = 0;
        ended = False;

        for oy in range(0, source.height):
            line = [];
            for ox in range(0, source.width):
                orig = source.rgb[oy][ox];

                if ended and ox != source.width-1 and ox != 00:
                    #show nop
                    # if ox > 0:
                    line.append( self.getColor(10, orig) );
                elif ox == 0 and oy > 0:
                    #always left

                    front = self.getColor(9, orig);
                    # donothing = "";
                elif ox == source.width-1:
                    if oy % 2 == 1:
                        line.reverse();

                    # add left turn to the front
                    if oy > 0:
                        line.reverse();
                        line.append( front );
                        line.reverse();

                    #right turns to the right
                    line.append( self.getColor( 8, orig) );



                else:
                    line.append( self.getColor('><+-.,[]'.index(data[pushed]) , orig) );
                    pushed += 1;
                    if pushed == len(data):
                        ended = True;
            print len( line );
            colors.append(line);
            line = [];
            front = None;

        print "";
        print len(colors);
        print len(colors[0]);

        return colors;

    def getColor(self, number, color):
        # print number;
        # print color;
        i = (-2*color[0] + 3*color[1] + color[2]) % 11;

        b = color[2];
        if color[2] > 11:
            b = color[2] - 11 + (number - i);
        elif color[2] < 255-11:
            b +=  11 + number - i ;
        else:
            b += number - i ;
        # print "Before: {0}, after: {1}".format(i, (-2*color[0] + 3*color[1] + b) % 11);
        return (color[0], color[1], b);

    def render(self):
        print self.output;