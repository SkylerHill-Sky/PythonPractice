import numpy as np

from src.counting_elements.frog_river_one import *
from src.counting_elements.max_counters import *
from src.counting_elements.perm_check import *

from tictoc import tic, toc

def test_frog_river_one():
    pass    # is not done yet

def test_max_counters():
    # my_list = [0 for x in range(0,n)]
    test_arr = np.random.randint(1,99999,999999)
    n = max(test_arr) - 1

    # tic()
    a = max_counters(n, test_arr)
    # toc('hi')
    # ! need to add assert, coming back later
    # tic()
    # b = solution(n, test_arr)
    # toc()

def test_perm_check():
    assert perm_check([4, 1, 3, 2])
    assert perm_check([1,2,4]) == 0
    assert perm_check([1,2,3,4]) == 1
    assert perm_check([10000000]) == 0
    assert perm_check([1]) == 1
    assert perm_check([x for x in range(1,99999) if x != 78] ) == 0

def test_all_counting_elements():
    test_frog_river_one()
    test_max_counters()
    test_perm_check()

test_all_counting_elements()
