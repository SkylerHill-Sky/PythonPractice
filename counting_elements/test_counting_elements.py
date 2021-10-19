# __all__ = ['frog_river_one','max_counters','perm_check']
# from counting_elements import *

# my_list = [0 for x in range(0,n)]
from tictoc import tic, toc
import numpy as np

test_arr = np.random.randint(1,99999,999999)
n = max(test_arr) - 1

tic()
a = max_counters.max_counters(n, test_arr)
toc()

tic()
b = solution(n, test_arr)
toc()


assert a == b