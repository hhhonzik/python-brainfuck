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
        # print args;
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
        program = self.controller('bc2bf', 'test_data/helloworld.bc.png');
        output = program.run();

        self.assertEqual(program.output, '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.');



    def test_bl_01(self):
        """vynulování aktuální, ale pouze aktuální, buňky"""
        program = self.controller('bf2bl', 'test_data/hello1.b', 'testbl.png');
        output = program.run();

        self.assertEqual(program.output, "BrainFuck code Written to testbl.png");


        # porovnani souboru
        # je to soubor

        file1 = b'';
        with open("./testbl.png", mode="rb") as _file:
            file1 += _file.read()

        file2 = b'';
        with open("./test_data/helloworld.bl.png", mode="rb") as _file:
            file2 += _file.read()

        self.assertEqual(file1, file2);





    def test_bl_02(self):
        program = self.controller('bf2bl', '+');
        output = program.run();
        self.assertEqual(program.output, None);



    def test_bl_03(self):
        program = self.controller('bc2bl', 'test_data/helloworld.bc.png', 'test.bc2bl.png');
        output = program.run();
        self.assertEqual(program.output, "BrainFuck code Written to test.bc2bl.png");


        file1 = b'';
        with open("./test.bc2bl.png", mode="rb") as _file:
            file1 += _file.read()

        file2 = b'';
        with open("./test_data/helloworld.bl.png", mode="rb") as _file:
            file2 += _file.read()

        self.assertEqual(file1, file2);

    def test_bc_04(self):
        program = self.controller('bl2bc', 'test_data/helloworld.bl.png', 'test.bl2bc.png', 'test_data/test.bc.png');
        output = program.run();

        self.assertEqual(program.output, "Code Written to test.bl2bc.png");

        file1 = b'';
        with open("./test.bl2bc.png", mode="rb") as _file:
            file1 += _file.read()

        file2 = b'';
        with open("./test_data/helloworld.bc.png", mode="rb") as _file:
            file2 += _file.read()

        self.assertEqual(file1, file2);


    def test_bc_05(self):
        program = self.controller('bf2bc', 'test_data/hello1.b', 'test.bf2bc.png', 'test_data/test.bc.png');
        output = program.run();
        self.assertEqual(program.output, "Code Written to test.bf2bc.png");

        file1 = b'';
        with open("./test.bf2bc.png", mode="rb") as _file:
            file1 += _file.read()

        file2 = b'';
        with open("./test_data/helloworld.bc.png", mode="rb") as _file:
            file2 += _file.read()

        self.assertEqual(file1, file2);




#
# zajištění spuštění testů při zavolání souboru z příkazové řádky
#
if __name__ == '__main__':
    unittest.main()
