"""
    Compute number of distinct values in an array.
"""
# not efficient
# def solution(a):
#     b = []
#     for item in a:
#         if item not in b:
#             b.append(item)

#     return len(b)

# efficient
def distinct(a):
    b = set(a)  
    return len(b)
# converting from list to set my be big O(n)
# O(N*log(N)) or O(N)

# todo see if there's a more efficient way than mapping to a set/dictionary
