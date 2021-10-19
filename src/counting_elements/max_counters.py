"""
Calculate the values of counters after applying all alternating operations:
    increase counter by 1; set value of all counters to current maximum.
"""
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

# might delete this, coming back to clean up
# not my solution, from stack overflow - it's slower than mine but got a better score - what gives!
# def solution(n, a):
#     res = [0] * n
#     max_val = 0
#     last_update = 0

#     for i in a:
#         if 1 < i < n+1:
#             if res[i-1] < last_update:
#                 res[i-1] = last_update

#             res[i-1]+=1
            
#             if res[i-1] > max_val:
#                 max_val = res[i-1]
#         else:
#             last_update = max_val

#     for i in range(len(res)):
#         if res[i] < last_update:
#             res[i] = last_update

#     return res
    