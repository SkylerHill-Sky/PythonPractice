
def max_counters(n, a):
    l = [0] * n
    
    for i in a:
        if i == n+1:
            l = [max(l)] * n
            # increase all to maximum value
        elif 1 <= i <= n:
            l[ i-1 ] += 1
        else:   #i > n+1
            # this isn't clear how to handle this based on the prompt, I could handle bad input with:
            # raise  ValueError("the prompt states this number should be between 1 and n+1 ")
            pass

    return l

# not my solution, from stack overflow - it's slower than mine but got a better score - what gives!
def solution(N, A):
    res = [0] * N
    max_val = 0
    last_update = 0

    for i in A:
        if 1 < i < n+1:
            if res[i-1] < last_update:
                res[i-1] = last_update

            res[i-1]+=1
            
            if res[i-1] > max_val:
                max_val = res[i-1]
        else:
            last_update = max_val

    for i in range(len(res)):
        if res[i] < last_update:
            res[i] = last_update

    return res
    