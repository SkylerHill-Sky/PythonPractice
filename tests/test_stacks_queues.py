from src.stacks_queues.brackets import *

# from tictoc import tic, toc

def test_brackets():
    str = "{[()](){}}"*999
    # a should be quicker than b
    # tic()
    a = solve(str)
    # toc()

    # tic()
    b = balance(str)
    # toc()

    assert a == b


def test_all_stacks_queues():
    test_brackets()

test_all_stacks_queues()
