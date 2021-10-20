from src.prefix_sums.min_avg_two_slice import *
from src.prefix_sums.passing_cars import *

import numpy as np


def test_min_avg_two_slice():
    # todo come back to this one
    pass

def test_passing_cars():
    arr = np.random.randint(0,1,5999)

    # commenting out because the method below is much faster
    # don't want to work my pc, but for notes compare the _new function to the old
    # assert passing_cars(arr) == 0
    assert  passing_cars_new(arr) == 0


def test_all_prefix_sums():
    test_min_avg_two_slice()
    test_passing_cars()

test_all_prefix_sums()
