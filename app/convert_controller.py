# -*- coding: utf-8 -*-
import parsers;
import coders;

class ConvertController:

    """
        Init function to initialize command line args into our flow.
    """
    def __init__(self, type, file, output = None, source = None):

        if type == None:
            self.type = "brainfuck" #default
        else:
            self.type = type;

        self.file = file;
        self.source = source;
        self.output = output
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
        elif self.type in ["bf2bc", "bl2bc"]:

            if self.output == None:
                self.error("Invalid output file: {0}".format(self.output));
            else:

                if self.type == "bl2bc":
                    # load input to BrainFuck code
                    converter = ConvertController('bl2bf', self.file, False, False);
                    converter.run();
                    self.file = converter.output;

                #initialize parser
                self.parser = self.initialize(self.type);
                self.instance = self.parser( self.file, self.output, self.source );
                self.output = self.instance.output;



        elif self.type in ["bf2bl", "bc2bl"]:

            if self.output == None:
                self.error("Invalid output file: {0}".format(self.output));
            else:

                if self.type == "bc2bl":
                    # load input to BrainFuck code
                    converter = ConvertController('bc2bf', self.file, False, False);
                    converter.run();
                    self.file = converter.output;

                #initialize parser
                self.parser = self.initialize(self.type);

                self.instance = self.parser( self.file, self.output );

                self.output = self.instance.output;


        else:
            self.error("Invalid import type: {0}".format(self.type));


        return self;

    def render(self):
        print self.output
        # self.instance.render();


    def initialize(self, name):
        return {
            'bc2bf': parsers.BrainCopter,
            'bl2bf': parsers.BrainLoller,
            'bf2bl': coders.BrainLoller,
            'bc2bl': coders.BrainLoller,
            'bf2bc': coders.BrainCopter,
            'bl2bc': coders.BrainCopter,

        }.get(name);

    """
        Error writing
    """
    def error(self, msg):

        print "Program error: {0}".format(msg)
        pass;







