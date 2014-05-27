# -*- coding: utf-8 -*-
import math, sys, types;
from interface import parserInterface;



class BrainFuck (parserInterface):
    """Interpretr jazyka brainfuck."""

    def __init__(self, data, memory=b'\x00', memory_pointer=0):
        """Inicializace interpretru brainfucku."""

        # print self.data;
        if data is types.FileType:
            self.data = data.read();
        else:
            self.data = data;


        # file load
        # data programu
        try:
            # je to soubor
            with data as _file:
                self.data = _file.read()
        except:
            # výjimka -> rovnou data
            self.data = data

        # inicializace proměnných
        self.memory = bytearray(memory);
        self.memory_pointer = memory_pointer

        # a) paměť výstupu
        self.output = ''


        # !?
        self.input_pointer = 0;
        if '!' in self.data:
            exc = self.data.index('!') +1 # chceme pozici znaku za vykřičníkem -> +1
            # očekáváme vstup
            if exc+1 < len(self.data):
                # uložíme vstup
                self.input = self.data[exc:]
                # a odstraníme ho z kódu
                self.data = self.data[:exc]
            else:
                self.input = ''
        else:
            self.input = ''


        self.decode(self.data);


    #
    # Operator functions
    #
    def getOperator(self, item):
        return {
            ">": self.operatorRight,
            "<": self.operatorLeft,
            "+": self.operatorPlus,
            "-": self.operatorMinus,
            ".": self.operatorEcho,
            ",": self.operatorLoad,
            "[": self.operatorFor
        }.get(item);


    # <for> - start cyklu
    def operatorFor(self, code):
        lefts = 1 #  sum( [ )
        rights = 0 # sum( ] )

        i = 1    # prvni je [

        while i < len(code):
            if code[i] == '[':
                lefts += 1
            elif code[i] == ']':
                rights += 1
            if lefts == rights:
                break
            i += 1

        while self.memory[self.memory_pointer] != 0:
            self.decode(code[1:i]);

        return i + 1; #posunout o 1


    # nacteni hodnoty
    def operatorLoad(self):
        if len(self.input) == 0 or self.input_pointer == len(self.input):
            self.memory[self.memory_pointer] = ord(sys.stdin.read(1))
        else:
            self.memory[self.memory_pointer] = ord(self.input[self.input_pointer])
            self.input_pointer += 1


    # vypis bunky
    def operatorEcho(self):
        val = chr(self.memory[self.memory_pointer]);
        self.output += val;
        # print val;


    # snizenihodnoty bunky
    def operatorMinus(self):
        if self.memory[self.memory_pointer ] == 0:
            self.memory[self.memory_pointer ] = 255;
        else:
            self.memory[self.memory_pointer ] -= 1;



    # zvyseni hodnoty bunky
    def operatorPlus(self):
        self.memory[self.memory_pointer ] = (self.memory[self.memory_pointer ] + 1) % 256;

    # posun doprava
    def operatorRight(self):
        self.memory_pointer += 1
        # zvyseni pole
        if self.memory_pointer == len(self.memory):
            self.memory += bytearray([0])

    def operatorLeft(self):
        # minimalni hodnota 0
        self.memory_pointer = max(0, self.memory_pointer - 1);

    #
    # BrainFuck decoder
    #
    def decode(self, code):
        i = 0;
        while i < len(code):
            operator = self.getOperator(code[i] );
            if operator == None:
                print "Neexistujici operator: {0}:{1}".format(i,code[i]);
                i += 1;
            else:
                if code[i] == "[":
                    i += operator(code[i:]); #  add string
                else:
                    operator();
                    i += 1;


    #
    # pro potřeby testů
    #
    def get_memory(self):
        # Nezapomeňte upravit získání návratové hodnoty podle vaší implementace!
        return self.memory

    #
    # output
    #
    def render(self):
        print self.output;

