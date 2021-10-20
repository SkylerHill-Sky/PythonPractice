from src.sorting.distinct import *
from src.sorting.num_disc_intersections import *


def test_distinct():
    arr = [2,1,1,2,3,1]
    assert distinct(arr) == 3

def test_num_disc_intersections():
    arr = [1,5,2,1,4,0]
    assert solution(arr) == 11

def test_all_sorting():
    test_distinct()
    test_num_disc_intersections()

test_all_sorting()