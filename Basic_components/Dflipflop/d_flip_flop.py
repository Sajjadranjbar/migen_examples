from migen import *


class Dflipflop(Module):
    def __init__(self, D, Q, Qi):
        self.sync += Q.eq(D)
        self.comb += Qi.eq(~Q)
