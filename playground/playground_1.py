from tictoc import tic, toc
import numpy as np
import random



def solution_1(a):
    min = 1
    a.sort()

    indexStart = 0

    for x in a:
        if x < 1:
            continue

        if min < x:
            return min
        else:
            min = x + 1

    return min

def solution(N):
    a = [random.randint(1,99) for x in range(N)]
    a[N-1] = 0
    return a

# print(solution(5))
# A = [1, 3, 6, 4, 1, 2]
# tic()
# a = solution_1(A)
# toc()



def lengthOfLongestSubstring( s) -> int:
    substrings = []
    longestSubString = ''
    currentSubstring = ''

    for c in s:
        if c in substrings:
            if len(currentSubstring) > len(longestSubString):
                longestSubString = currentSubstring

            substrings.clear()
            currentSubstring = ''
        else:
            currentSubstring += c
            substrings.append(c)

    return len(longestSubString)


print( lengthOfLongestSubstring('bbbbb'))