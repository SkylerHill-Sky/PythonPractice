def SerialNumberOld(strPar):
    try:
        strings = strPar.split('.') # 1 create a list of all of the substrings
        if(len(strings) != 3): # 1 verify that it's only 3 substrings
            return False

        numbers = []
        for i in range(3):
            numbers.append( list(map(int, strings[i])) ) # 1 check that it's all digits
        print(strings, numbers)

        for i in range(3):
            if not (numbers[i][2] > numbers[i][1] and numbers[i][2] > numbers[i][0]) :
                return False    # 4 check that the last digit is the greatest in each substring
        
        if ( (numbers[0][0] + numbers[0][1] + numbers[0][2]) % 2 ) != 0 :
            return False    # 2 must be even
        if ( (numbers[1][0] + numbers[1][1] + numbers[1][2]) % 2 ) == 0 :
            return False    # 3 must be odd

    except Exception as e:
        print(e)
        return False

    return True

# using list comprehension to make more readable than up above
def SerialNumberWithListComprehension(strPar):
    try:
        strings = strPar.split('.') # 1 create a list of all of the substrings
        if(len(strings) != 3): # 1 verify that it's only 3 substrings
            return False

        # 1 check that it's all digits
        first, second, third = [ list(map(int, strings[i])) for i in range(3) ]
        print(strings, first, second, third)

        # 4 check that the last digit is the greatest in each substring
        for numbers in [first, second, third]:
            if not (numbers[2] > numbers[1] and numbers[2] > numbers[0]) :
                return False

        if ( sum(first) % 2 ) != 0 :
            return False    # 2 must be even
        if ( sum(second) % 2 ) == 0 :
            return False    # 3 must be odd

    except Exception as e:
        print(e)
        return False

    return True

print( SerialNumberOld('123.124.123') )
print( SerialNumberWithListComprehension('123.124.123') )