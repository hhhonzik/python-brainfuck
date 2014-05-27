__author__ = 'honzicek'
import Parser

class Controller:


    """
        Init function to initialize command line args into our flow.
    """
    def __init__(self, args):
        self.args = args;
        pass


    """
        Main function that will first check existing libraries and their requirements
    """
    def run(self):
        if len(self.args) == 1:
            print "No import type specified!"
            return self.help()

        if len(self.args) < 3:
            print "No input specified!"
            return self.help()

        if self.args[1] in ["video", "gif", "images"]:

            #initialize parser
            self.parser = self.initializeParser(self.args[1])

            #parse input
            if self.parser.parseInput(self.args[2]):

                #initialize Generator
                print "Running conversion."
            else:
                print "Problem with importing, exiting .."

        else:
            print "Invalid import type!"
            self.help();


        pass

    def initializeParser(self, name):
        return {
            'images': Parser.Images(),
        }.get(name)

    """
        Help will write a quick usage manual to console
    """
    def help(self):


        file = self.args[0][self.args[0].rfind("/")+1:-1] + "y"

        print ""
        print "Example usage:"
        print ""
        print file + " video video.mp4 <delay_between_frames_in_ms>"
        print file + " gif file.gif"
        print file + " images images/*.png"





