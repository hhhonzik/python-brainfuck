#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# import modulu zodpovědného za testy jednotek
import unittest

######################### - Změny
import app.ImageParser as image_png # jine importy
from app.parsers.brainfuck import BrainFuck
from app.parsers.brainloller import BrainLoller
from app.ImageParser import PngReader
from app.convert_controller import ConvertController
######################### -/ Změny

#
# třída s dočasným „falešným“ výstupem
#

import sys

class FakeStdOut:
    def write(self, *args, **kwargs):
        pass
    def flush(self):
        pass



#
# třídy obsahující testy
#

class TestConverter(unittest.TestCase):
    """testuje chování interpretru brainfucku"""
    
    def setUp(self):
        self.controller = ConvertController
        self.out = sys.stdout
        sys.stdout = FakeStdOut()
    
    def tearDown(self):
        sys.stdout = self.out


    def test_bf_01(self):
        """vynulování aktuální, ale pouze aktuální, buňky"""
        program = self.controller('bl2bf', 'test_data/HelloWorld.png');
        output = program.run();

        self.assertEqual(program.output, '>+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.>>>++++++++[<++++>-]<.>>>++++++++++[<+++++++++>-]<---.<<<<.+++.------.--------.>>+.');

    def test_bf_02(self):
        """vynulování aktuální, ale pouze aktuální, buňky"""
        program = self.controller('bc2bf', 'test_data/HelloWorld.png');
        output = program.run();

        self.assertEqual(program.output, '>+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.>>>++++++++[<++++>-]<.>>>++++++++++[<+++++++++>-]<---.<<<<.+++.------.--------.>>+.');



#
# zajištění spuštění testů při zavolání souboru z příkazové řádky
#
if __name__ == '__main__':
    unittest.main()
