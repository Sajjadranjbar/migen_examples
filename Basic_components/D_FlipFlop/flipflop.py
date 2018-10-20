from migen import *
import migen.sim


class D_FF (Module):
    def __init__(self):
        self.D = D = Signal()
        self.Q = Q = Signal()
        self.counter = counter = Signal(3)

        self.comb += D.eq(counter[2])
        self.sync += Q.eq(D)
        self.sync += counter.eq(counter + 1)


def D_FF_TEST(dut):
    for i in range(20):
        print("{} {}".format((yield dut.counter), (yield dut.Q)))
        yield


dut = D_FF()
run_simulation(dut, D_FF_TEST(dut), vcd_name="dflipflop.vcd")
