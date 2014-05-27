#!/usr/bin/python

__author__ = 'honzicek'

import sys, argparse;

import app;


from app.parsers.brainfuck import BrainFuck


def main(argv=None):
    #sys args definition
    parser = argparse.ArgumentParser();
    parser.add_argument('file');
    parser.add_argument('--version', action='version', version='%(prog)s 0.1');
    parser.add_argument('-l', '--brainloller', dest="type", action="store_const", const="brainloller", help="Jde o program v jazyce brainloller.");
    parser.add_argument('-c', '--braincopter', dest="type", action="store_const", const="braincopter", help="Jde o program v jazyce braincopter.");

    args = parser.parse_args();


    # initialize controller
    controller = app.Controller(args.type, args.file);
    controller.run();
    controller.render();