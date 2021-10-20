"""
    Find the missing element in a given permutation.

    n = 99
    so array should = [] from 1-100

    which would mean len(a) == 99

    but if 100 is missing

    max(a) should = len(a) + 1 
    if its missing
        max(a) = len(a)

    handle base cases first, like empty or last index missing
"""

# def find_missing_number(a: set(int)):
def find_missing_number(a):
    b = set(range(1, len(a)+2))
    return ( b - set(a) ).pop()  # returns the element that it removes
