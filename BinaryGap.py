
# find longest substring of repeating zeros in binary of int
def binaryGap(N):

    binaryNum = str( bin(N)[2:] ) # start from 3rd index to remove binary syntax
    binaryNum = binaryNum.lstrip('0').rstrip('0') # strip leading and trailing zeros
    listOfZeros = binaryNum.split('1') # create a list of all of the zero strings

    max_gap = 0
    for i in range( len(listOfZeros) ):
        tempGap = len( listOfZeros[i] )
        if tempGap > max_gap:
            max_gap = tempGap

    return (max_gap)
    
print(binaryGap(1000000000000000000000000000))
