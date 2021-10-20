"""
    Compute the number of intersections in a sequence of discs.
    todo: I don't believe this solution is correct 
"""
def solution(a):
    intersections = 0
    eastBound = 0

    for i in range( len(a) ):
        for j in range(i+1, len(a)) :
            if i - a[i] >= j - a[j] or i + a[i] <= j + a[j]:
                intersections += 1

    return intersections

