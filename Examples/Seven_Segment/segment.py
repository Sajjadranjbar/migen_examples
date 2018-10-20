from migen import *
from migen.fhdl import verilog
import sys


class sevenseg_ctrl(Module):
    def __init__(self):
        self.abcdefg = abcdefg = Signal(7)
        self.hexa = hexa = Signal(4)
        table = [
            0x3f, 0x06, 0x5b, 0x4f,
            0x66, 0x6d, 0x7d, 0x07,
            0x7f, 0x6f, 0x77, 0x7c,
            0x39, 0x5e, 0x79, 0x71
        ]

        cases = {}
        for i in range(16):
            cases[i] = abcdefg.eq(table[i])

        self.comb += Case(hexa, cases)


example = sevenseg_ctrl()
file = open("segment.v", "w")
pStd = sys.stdout
sys.stdout = file
print(verilog.convert(example, {example.hexa, example.abcdefg}))
sys.stdout = pStd
file.close()
