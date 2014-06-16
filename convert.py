#!/usr/bin/python

__author__ = 'honzicek'

import sys;
import argparse;

import app;


from app.parsers.brainfuck import BrainFuck


def main(argv=None):
    #sys args definition
    parser = argparse.ArgumentParser();
    parser.add_argument('source');
    parser.add_argument('-o', '--output', dest="output", help="Output image for *2bl and *2bc conversions");
    parser.add_argument('-i', '--input', dest="input", help="Input image for bf2bc and bl2bc conversions");
    parser.add_argument('--version', action='version', version='%(prog)s 0.1');
    parser.add_argument('-t', '--type', dest="type", action="store", help="Specify type.", choices={"bc2bf","bl2bf", "bf2bl", "bc2bl", "bf2bc"});


    args = parser.parse_args();

    if args.type in ["bf2bl"]:
        if args.output is None:
            parser.error('Output is required');


    if args.type in ["bf2bc", 'bl2bc']:
        if args.input is None:
            parser.error('Input file is required');


    # initialize controller
    controller = app.ConvertController(args.type, args.source, args.output, args.input);
    controller.run();
    controller.render();


if __name__ == "__main__":
    sys.exit(main())