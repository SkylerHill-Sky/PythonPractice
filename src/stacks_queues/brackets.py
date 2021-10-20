"""
    Determine whether a given string of parentheses (multiple types) is properly nested.
"""


def solve(S):
    map_dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    openers = []

    for letter in S:
        if letter in map_dict.values():
            openers.append(letter)
        elif letter in map_dict.keys():
            if len(openers) == 0:
                return 0
            if openers.pop() != map_dict[letter]:
                return 0
                
    if len(openers) != 0:
        return 0
    
    return 1

openList = ["[", "{", "("]
closeList = ["]", "}", ")"]

def balance(myStr):
    stack = []
    for item in myStr:
        if item in openList:
            stack.append(item)
        elif item in closeList:
            pos = closeList.index(item)
            if (len(stack) > 0) and (openList[pos] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return 0
    if len(stack) == 0:
        return 1
        