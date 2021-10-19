from tictoc import tic, toc



def solution(a):
    intersections = 0
    eastBound = 0

    for i in range( len(a) ):
        for j in range(i+1, len(a)) :
            if i - a[i] >= j - a[j] or i + a[i] <= j + a[j]:
                intersections += 1

    return intersections

arr = [1,5,2,1,4,0]

tic()
x = solution(arr)
toc()

print(x)
