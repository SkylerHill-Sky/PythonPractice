from tictoc import tic, toc

# not efficient
def solution(a):
    b = []
    for item in a:
        if item not in b:
            b.append(item)

    return len(b)

# efficient
def solution_b(a):
    b = set(a)  
    return len(b)
# converting from list to set my be big O(n)
# O(N*log(N)) or O(N)

arr = [2,1,1,2,3,1]
tic()
x = solution(arr)
toc()

tic()
y = solution(arr)
toc()

print(x)
assert x == y