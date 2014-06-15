# BrainFuck

---

Brainfuck/Brainloller/Braincopter programming language interpreter.
Requires python2.7.

---

## Installation

Close this [repository](http://github.com/hhhonzik/python-brainfuck) or download [ZIP](http://github.com/hhhonzik/python-brainfuck/archive/master.zip)

---


## Documentation

    python brainx.py --help

## Examples

Brainfuck example:

    python brainx.py test_data/hello1.b

    python brainx.py "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++."

BrainLoller example:

    python brainx.py -l test_data/HelloWorld.png


BrainCopter example:

    python brainx.py -c test_data/TheLostKingdom.png


# B* Converter

---

Brainfuck/Brainloller/Braincopter programming language converter.
Requires python2.7.

---

## Documentation

This convertor use PNG-8 images.

    python brainx.py --help



## Examples

BrainLoller to BrainFuck example (bl2bf):

     python convert.py -t bl2bf test_data/HelloWorld.png


BrainCopter to BrainFuck example (bc2bf):

     python convert.py -t bc2bf test_data/TheLostKingdom.png


BrainFuck to BrainLoller example (bf2bl):

     python convert.py -t bf2bl -o hello.png ./test_data/hello1.b

BrainCopter to BrainLoller example (bc2bl):

     python convert.py -t bc2bl -o hello.png ./test_data/hello1.b


