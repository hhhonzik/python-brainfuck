# BrainFuck Interpretor

---

Brainfuck/Brainloller/Braincopter programming language interpreter.

Compatible with python3 and [python2.7](https://github.com/hhhonzik/python-brainfuck/tree/python2.7).

---

## Installation

Clone this [repository](http://github.com/hhhonzik/python-brainfuck) or download [ZIP](http://github.com/hhhonzik/python-brainfuck/archive/master.zip)

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

    python convert.py --help



## Examples

### *2bl

BrainFuck or BrainCopter to BrainLoller.

BrainFuck to BrainLoller example (bf2bl):

     python convert.py -t bf2bl -o hello.png ./test_data/hello1.b

BrainCopter to BrainLoller example (bc2bl):

      python convert.py -t bc2bl -o hello.png ./test_data/bc_helloworld.png


### *2bc

BrainFuck or BrainLoller to BrainCopter, you need to specify source image and brainfuck or brainloller code

BrainFuck to BrainCopter example (bf2bc):

     python convert.py -t bf2bc -i test_data/temp.png -o hello2.png test_data/hello1.b

BrainLoller to BrainCopter example (bl2bc):

     python convert.py -t bl2bc -i test_data/temp.png -o hello3.png test_data/HelloWorld.png



### *2bf

BrainLoller to BrainFuck example (bl2bf):

     python convert.py -t bl2bf test_data/HelloWorld.png


BrainCopter to BrainFuck example (bc2bf):

     python convert.py -t bc2bf test_data/TheLostKingdom.png




