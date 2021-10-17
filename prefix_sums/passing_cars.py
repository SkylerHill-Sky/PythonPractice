from tictoc import tic, toc
import numpy as np


def passing_cars(a):
    cars = 0
    try:
        for i, p in enumerate(a):
            if p == 0:
                # del a[]
                for j in range(i+1, len(a)) :
                    if a[j] == 1:
                        cars +=1 # (1,0)  tuple notation in python
    
    except: # incase we get an index out of bound exception, - I don't want to check "if cars > 1000000000" len(a) times
        if cars > 1000000000:
            return -1

    if cars > 1000000000:
            return -1
    return cars

# much faster
def passing_cars_new(a):
    pairs = 0
    eastBound = 0
    for i in range( len(a) ):
        if a[i] == 0:
            eastBound  += 1
        elif a[i] == 1:
            pairs += eastBound 
        
        if pairs > 1000000000:
            return -1

    return pairs

"""
p   w/ q (0,1)    w/2ndQ is (0,3)   w/3rdQ is (0,4) 
q  
p  (2,3)   (2,4)
q
q
"""
arr = np.random.randint(0,1,5999)
# tic()
# a = passing_cars(arr)
# toc()

tic()
b = passing_cars_new(arr)
toc()

assert a == b
