
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


def solution(a):
    count_pairs = {}
    for item in a:
        if item in count_pairs:
            count_pairs[item] += 1
        else:
            count_pairs[item] = 1

    for val in count_pairs.values():
        if val % 2 !=0:
            return False
    
    return True




a = [1,2,2,1,3,4,3,4,3,3]
print(solution(a))