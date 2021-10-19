from tictoc import tic, toc
import numpy as np



def solution_1(a):
    min = 1
    a.sort()

    indexStart = 0

    for x in a:
        if x < 1:
            continue

        if min < x:
            return min
        else:
            min = x + 1

    return min

import random
def solution(N):
    a = [random.randint(1,99) for x in range(N)]
    a[N-1] = 0
    return a


print(solution(5))



def solution_3():
    


    pass


A = [1, 3, 6, 4, 1, 2]
tic()
a = solution_1(A)
toc()

print(a)