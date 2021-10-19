from tictoc import tic, toc
import numpy as np



def solution(S):
    seen = {}
    strings = 1

    for c in S:
        if c in seen:
            seen.clear()
            seen[c] = 1
            strings += 1
        else:
            seen[c] = 1

    return strings





A = [1, 3, 6, 4, 1, 2]
tic()
a = solution('dddde')
b = solution('cycle')
toc()

print(a, b)