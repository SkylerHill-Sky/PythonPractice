from math import sqrt, floor

# largest number would be 2^16
def is_prime(num):
    for x in range( 2, floor( sqrt(num)) ):
        if num % x == 0:
            # print("It's divisible by", x)
            return False

    return True
