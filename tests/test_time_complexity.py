from src.time_complexity.frog_jump import *
from src.time_complexity.perm_missing_elem import *
from src.time_complexity.tape_equlibrium import *


def test_frog_jump():
    assert frog_jump(10, 85, 30) == 3

def test_perm_missing_elem():
    assert find_missing_number([1,2]) == 3
    assert find_missing_number([]) == 1
    assert find_missing_number([1,3]) == 2

    arr = [x for x in range(1,99) if x != 78]  # more list comprehnsion
    assert find_missing_number(arr) == 78
    # or arr = list(range(1,99)).pop(78)

def test_tape_equilibrium():
    pass    # todo

def test_all_time_complexity():
    test_frog_jump()
    test_perm_missing_elem()
    test_tape_equilibrium()

test_all_time_complexity()