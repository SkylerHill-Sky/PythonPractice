"""
Rotate an array to the right by a given number of steps.
"""

def rotate_array(A, K):
    try:
        for i in range(K):
            pop_item = A.pop()
            A.insert(0, pop_item)
    except Exception as e:
        print(e)
        return A
    
    return A  
