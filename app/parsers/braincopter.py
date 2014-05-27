# -*- coding: utf-8 -*-
import math, sys, types;
from interface import parserInterface;
from brainloller import BrainLoller;
from ..ImageParser import PngReader;


class BrainCopter (BrainLoller):
    """A class to process brainloller language."""


    def getoperation(self, color):
        i = (-2*color[0] + 3*color[1] + color[2]) % 11

        if i < 8:
            self.char = '><+-.,[]'[i];
            return self.normalChar;
        elif i == 8:
            self.right;
        elif i == 9:
            self.left;

        return res, d

    def normalChar(self, d):
        return self.char, d;