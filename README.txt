KOMENTÁŘE K SEMESTRÁLNÍ PRÁCI
    verze 2013.1



Konstruktor brainfucku má následující potřebné parametry:
    BrainFuck(CESTA|DATA)
        ~ inicializace s daty programu jako cesta ke zdrojovému textovému souboru nebo jako řetězec a jeho vykonání
    BrainFuck().output
        ~ řetězec výstupu, který vyprodukuje běžící program voláním brainfuckovského příkazu '.'
    BrainFuck().memory_pointer
        ~ ukazatel do paměti/pásky
    BrainFuck().get_memory()
        ~ vrací aktuální stav paměti/pásky jako binární řetězec ('bytes()')
Jeho plné volání je následující (což je také implicitní nastavení parametrů 'memory' a 'memory_pointer'):
    BrainFuck(CESTA|DATA, memory=b'\x00', memory_pointer=0)
Toto plné volání se uplatňuje pouze v testech, jinak stačí zadat cestu ke zdrojovému souboru brainfucku nebo přímo vlastní kód jako řetězec.



Konstruktor PNG-obrázku má následující potřebné parametry:
    PngReader(CESTA)
        ~ inicializace cestou k obrázku
    PngReader().rgb
        ~ seznam barvových dat obrázku v podobě seznamů řádek obsahujících RGB-trojce, tj.
            [
                # 1. řádka o n sloupcích
                [ (R01, G01, B01), ...,  (R0n, G0n, B0n)],
                ...
                # m-tá řádka o n sloupcích
                [ (Rm1, Gm1, Bm1), ...,  (Rmn, Gmn, Bmn)],
            ]
Vaše interní reprezentace může být samozřejmě úplně jiná, ale pro potřeby testů musíte poskytnout atribut 'rgb' s uvedenou strukturou.
Kromě toho vyhodí PngReader následující výjimky:
    PNGWrongHeaderError
        ~ předložený soubor není PNG
    PNGNotImplementedError
        ~ předložený soubor je sice PNG, ale používá části standardu, které jsme neimplementovali (musíte podporovat pouze IHDR-hlavičku 'mn82000', kde 'm' a 'n' jsou šířka a výška obrázku v pixelech)



Konstruktor brainlolleru/braincopteru má následující potřebné parametry:
    BrainLoller(CESTA)
    BrainCopter(CESTA)
        ~ inicializace s daty programu jako cesta ke zdrojovému PNG-obrázku a jeho následné vykonání
    BrainLoller().data
    BrainCopter().data
        ~ výsledný zdrojový kód brainfucku po rozkódování obrazových dat (tedy pouze základních 8 brainfuckovských operací)
    BrainLoller().program
    BrainCopter().program
        ~ odkaz na instanci 'BrainFuck( BrainLoller().data )', resp. 'BrainFuck( BrainCopter().data )' -- aby bylo možné otestovat výstup programu, případně i pozici ukazatele do paměti a paměť samotnou



Program se bude k uživateli chovat přívětivě, tzn. bude umět vyhodnotit špatné vstupy a poskytne nápovědu, přibližně něco jako následující dvě ukázky:

$> python3.2 __main__.py
usage: __main__.py [-h] [--version] [-l] [-c] file
__main__.py: error: too few arguments

$> python3.2 __main__.py --help
usage: __main__.py [-h] [--version] [-l] [-c] file

positional arguments:
  file               Soubor ke zpracování.

optional arguments:
  -h, --help         show this help message and exit
  --version          show program's version number and exit
  -l, --brainloller  Jde o program v jazyce brainloller.
  -c, --braincopter  Jde o program v jazyce braincopter.

Program, který pustím bez parametrů a on nic nevrátí a nechá uživatele „plavat“, rovnou vrátím!
