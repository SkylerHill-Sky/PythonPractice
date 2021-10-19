"""
Find longest sequence of zeros in binary representation of an integer.
    : find longest substring of repeating zeros in binary of int
"""

def binary_gap(N):
    
    binary_num = str( bin(N)[2:] ) # start from 3rd index to remove binary syntax
    binary_num = binary_num.lstrip('0').rstrip('0') # strip leading and trailing zeros
    list_zeros = binary_num.split('1') # create a list of all of the zero strings

    max_gap = 0
    for item in list_zeros:
        temp_gap = len( item )
        if temp_gap > max_gap:
            max_gap = temp_gap

    return (max_gap)
