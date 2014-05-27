# -*- coding: utf-8 -*-
import parsers;

class Controller:

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
        if self.type in ["brainloller", "braincopter", "brainfuck"]:

            #initialize parser
            self.parser = self.initialize(self.type);


            try:
            # je to soubor
                with open(self.file, mode='r') as _file:
                    data = _file.read();
            except:
                # výjimka -> rovnou data
                data = self.file;



            self.instance = self.parser( data );

        else:
            self.error("Invalid import type: {0}".format(self.type));


        return self;

    def render(self):
        self.instance.render();

    def initialize(self, name):
        return {
            'brainfuck': parsers.BrainFuck,
            #'brainloller': Parser.brainloller(),
            #'braincopter': Parser.braincopter()
        }.get(name);

    """
        Error writing
    """
    def error(self, msg):

        print "Program error: {0}".format(msg)
        pass;







