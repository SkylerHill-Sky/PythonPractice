"""
    A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

    For example, in array A such that:

    A[0] = 9  A[1] = 3  A[2] = 9
    A[3] = 3  A[4] = 9  A[5] = 7
    A[6] = 9
    the elements at indexes 0 and 2 have value 9,
    the elements at indexes 1 and 3 have value 3,
    the elements at indexes 4 and 6 have value 9,
    the element at index 5 has value 7 and is unpaired.

    Given an array A consisting of N integers fulfilling the above conditions,
    returns the value of the unpaired element.
"""


# find odd occurence by sorting
def odd_occurences_with_sort(A):     
    if len(A) == 1:
        return A[0]

    A.sort()

    for i in range(0 , len(A)-1 , 2):    # moving up twice at a time 
        if A[i] != A[i+1]:  # comparing next index
            return A[i]
    return A[i]

"""
    find odd occurence by taking difference with exclusive or

    if we exclusive or all of the numbers it should equal zero
    else it would be the difference
"""
def odd_occurences_with_exclusive_or(a: [int]) -> int: 
    diff = 0
    for number in a:
        diff ^= number
    return diff