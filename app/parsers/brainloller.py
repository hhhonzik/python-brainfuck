# -*- coding: utf-8 -*-
import math, sys, types;
from interface import parserInterface;
from brainfuck import BrainFuck;
from ..ImageParser import PngReader;

class BrainLoller (parserInterface):
    """A class to process brainloller language."""

    def __init__(self, filename):

        img = PngReader(filename);

        self.data = self.decode(img.rgb);

        self.program = BrainFuck(self.data);

    def decode(self, data):
        """Parsing PNG file and returning BrainFuck code."""

        res = ''

        # pozice: x, y, start na [0, 0]
        # směr, start 1:
        x = y = 0
        d = 1

        # print len(data);
        # print len(data[0]);
        while True:
            if x < 0 or y < 0 or y >= len(data) or x >= len(data[0]):
                break;
            else:
                operation = self.getoperation( data[y][x] );
                if operation:
                    output, d = operation(d);
                    res += output
                x, y = self.move(x, y, d)



        return res
    def getoperation(self, name):

        return {
            (255,0,0): self.opLeft,
            (128,0,0): self.opRight,
            (0,255,0): self.opPlus,
            (0,128,0): self.opMinus,
            (0,0,255): self.opEcho,
            (0,0,128): self.opLoad,
            (255,255,0): self.opForStart,
            (128,128,0): self.opForEnd,
            (0,255,255): self.right,
            (0,128,128): self.left

        }.get(name);

    def opLeft(self,d):
        return ">",d;
    def opRight(self,d):
        return "<", d;
    def opPlus(self,d):
        return "+",d;
    def opMinus(self,d):
        return "-",d;
    def opEcho(self,d):
        return ".",d;
    def opLoad(self,d):
        return ",",d;
    def opForStart(self,d):
        return "[",d;
    def opForEnd(self,d):
        return "]",d;

    # zmena direction
    def left(self, d):
        return "", (d-1)%4;
    def right(self, d):
        return "", (d+1)%4;

    def move(self, x, y, d):
        """Move according to direction."""
        if d == 0:
            y -= 1
        elif d == 1:
            x += 1
        elif d == 2:
            y += 1
        elif d == 3:
            x -= 1

        return x, y

    def render(self):
        print self.program.output;