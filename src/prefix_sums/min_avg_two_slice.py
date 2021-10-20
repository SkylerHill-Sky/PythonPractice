"""
    Find the minimal average of any slice containing at least two elements.
"""
from tictoc import tic, toc
import numpy as np


# def solution(a):
#     start = 0
#     for i in range( len(a) ):
        

#         pass
    
    
#     return start

# todo comeback: ! this isn't working, i want to change this but i'm too tired
def solution(A):
    amin = sum(A)/len(A)
    imin = 0

    for i, p in enumerate(A):
        for j in range(i+1, len(A)):
            if j < len(A):
                p += A[j]
                aij = p/(j-i+1)

                if aij < amin:
                    amin = aij
                imin = i

    return imin

# arr = np.random.randint(0,9,99)
# arr = [4,2,2,5,1,5,8,1]

# tic()
# b = solution(arr)
# toc()

# print(b)
