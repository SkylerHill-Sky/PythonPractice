"""
    Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.

    todo: not done
"""

# a=[1,2,3,4,5]
# print(a[1:])
# print(a[1::])

# !NOT DONE
# TapeEquilibrium

def TapeEquilibrium(A):
    left = A[0]
    right = sum(A[1::])
    diff = abs(left - right)

    for p in range(1, len(A)):
        ldiff = abs(left - right)
        if ldiff < diff:
            diff = ldiff
        left += A[p]
        right -= A[p]

    return diff