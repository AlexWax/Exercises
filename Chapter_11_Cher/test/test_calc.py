from Study.Chapter_11_Cher.code.calc import Calc

def test_sum():
    assert Calc().sum(3, 2) == 5

def test_sub():
    assert Calc().sub(10, 3) == 6

def test_mul():
    assert Calc().mul(5, 5) == 25

def test_div():
    assert Calc().div(10, 3) == 3

def test_pow2():
    assert Calc().pow2(10) == 99

def test_invis():
    assert 23 == 1