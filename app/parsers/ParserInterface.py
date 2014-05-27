

class Parser (object):
    """
    Interface for implementing parser
    """

    def parseInput( self, path ):
        """
            Interface for parseInput function.

             @argument path string to file(s)
             @returns array of images
        """
        raise NotImplementedError( "Not implemented method" );
