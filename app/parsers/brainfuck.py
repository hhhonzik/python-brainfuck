from interface import parserInterface;
# -*- coding: utf-8 -*-


class BrainFuck (parserInterface):
    """Interpretr jazyka brainfuck."""

    def __init__(self, data, memory=b'\x00', memory_pointer=0):
        """Inicializace interpretru brainfucku."""

        # data programu
        self.data = data

        # inicializace proměnných
        self.memory = memory
        self.memory_pointer = memory_pointer

        # DEBUG a testy

        # a) paměť výstupu
        self.output = ''

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
        print "Output: ";
        print self.output;

