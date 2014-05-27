# -*- coding: utf-8 -*-
import parsers;

class ConvertController:

    """
        Init function to initialize command line args into our flow.
    """
    def __init__(self, type,
                 file):

        if type == None:
            self.type = "brainfuck" #default
        else:
            self.type = type;

        self.file = file;
        pass

    """
        Main function that will first check existing libraries and their requirements
    """
    def run(self):
        if self.type in ["bc2bf", "bl2bf"]:

            #initialize parser
            self.parser = self.initialize(self.type);

            self.instance = self.parser( self.file, decodeBF=True );
            self.output = self.instance.output;

        else:
            self.error("Invalid import type: {0}".format(self.type));


        return self;

    def render(self):
        print self.output
        # self.instance.render();


    def initialize(self, name):
        return {
            'bc2bf':   parsers.BrainCopter,
            'bl2bf': parsers.BrainLoller,
        }.get(name);

    """
        Error writing
    """
    def error(self, msg):

        print "Program error: {0}".format(msg)
        pass;







