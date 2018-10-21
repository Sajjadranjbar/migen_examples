from d_flip_flop import Dflipflop
from migen.sim import run_simulation
from migen.fhdl.structure import Signal

ff_D = Signal()
ff_Q = Signal()
ff_Qi = Signal()

ff = Dflipflop(ff_D, ff_Q, ff_Qi)


def testbench():
    yield ff_D.eq(1)
    yield
    yield ff_D.eq(0)
    yield
    yield
    yield ff_D.eq(1)
    yield
    yield
    yield
    yield ff_D.eq(0)
    yield
    yield


run_simulation(ff, testbench(), vcd_name="test_d_ff.vcd")
