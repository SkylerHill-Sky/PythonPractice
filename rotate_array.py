# def rotateArray(A, K):
#     temp = []
#     i = 0
#     while (i < K):
#         temp.append(A[i])
#         i = i + 1
#     i = 0
#     while (K < len(A)):
#         print(A, i, K)
#         A[i] = A[K]
#         i += 1
#         K += 1
#     print(temp)
#     print(A)
#     A[:] = A[: i] + temp
#     print(A)
#     return A

def rotate_array(A, K):
    for i in range(K):
        pop_item = A.pop()
        A.insert(0, pop_item)
    
    return A  

print(rotate_array([1, 2, 3, 4], 2))