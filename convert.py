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
    parser.add_argument('--version', action='version', version='%(prog)s 0.1');
    parser.add_argument('-t', '--type', dest="type", action="store", help="Specify type.", choices={"bc2bf","bl2bf"});


    args = parser.parse_args();


    # initialize controller
    controller = app.ConvertController(args.type, args.source);
    controller.run();
    controller.render();

if __name__ == "__main__":
    sys.exit(main())