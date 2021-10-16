# def perm_check(a):
#     b = set(range(1, max(a)+1)) if len(a)>1 else set(a)
#     if min(b)==1len(b) == len(a):
#         return 1
#     else:
#         return 0

# print(perm_check([1,2,4]))
# print(perm_check([1,2,3,4]))


def perm_check(a):
    if min(a) != 1 or max(a) != len(a):
        return 0
    if sorted(a) == list (range(1,max(a)+1) ):
        return 1
    else:
        return 0

assert perm_check([4, 1, 3, 2])
assert perm_check([1,2,4]) == 0
assert perm_check([1,2,3,4]) == 1
assert perm_check([10000000]) == 0
assert perm_check([1]) == 1
assert perm_check([x for x in range(1,99999) if x != 78] ) == 0