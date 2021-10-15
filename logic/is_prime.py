from math import sqrt, floor

# largest number would be 2^16
def is_Prime(num):
    for x in range( 2, floor( sqrt(num)) ):
        if num % x == 0:
            print("It's divisible by", x)
            return False

    return True

# print(is_Prime(1230987623144987))


# I wanted to say that I don't have as much experience with Python as I do with C#
# But I decided to use this as an opportunity to have fun with Python :) 
# So if some of my PEP8 stuff is off, or it looks like I organize my code like I have C# habits - that's why
