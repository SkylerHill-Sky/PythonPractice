
"""
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

arr = [1,2]
assert find_missing_number(arr) == 3
arr = []
assert find_missing_number(arr) == 1
arr = [1,3]
assert find_missing_number(arr) == 2
arr = [x for x in range(1,99) if x != 78]  # more list comprehnsion
assert find_missing_number(arr) == 78
# or arr = list(range(1,99)).pop(78)