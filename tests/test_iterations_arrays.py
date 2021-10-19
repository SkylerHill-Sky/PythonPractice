from src.iterations_arrays.binary_gap import *
from src.iterations_arrays.odd_occurences import *
from src.iterations_arrays.rotate_array import *

from tictoc import tic, toc
import numpy as np

def test_binary_gap():
    assert binary_gap(1000000000000000000000000020) == 22
    assert binary_gap(1231980198723948723948723) == 8

def test_odd_occurences():
    test_array = [6,5,4,3,2,1,0,1,2,3,4,5,6]
    a = odd_occurences_with_sort(test_array)
    b = odd_occurences_with_exclusive_or(test_array)
    assert a == b == 0
    test_array.append(7)
    a = odd_occurences_with_sort(test_array)
    b = odd_occurences_with_exclusive_or(test_array)
    assert a == b == 7

def test_rotate_array():
    pass

def test_iterations_arrays():
    test_binary_gap()
    test_odd_occurences()

test_iterations_arrays()