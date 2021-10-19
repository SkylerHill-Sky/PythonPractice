"""
Check whether array A is a permutation.
"""

def perm_check(a):
    if min(a) != 1 or max(a) != len(a):
        return 0
    if sorted(a) == list (range(1,max(a)+1) ):
        return 1
    else:
        return 0
