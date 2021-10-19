import pytest

from iterating_parsing import *
assert binary_gap.binary_gap(1000000000000000000000000020) == 22

assert is_prime.is_prime(1230987623144987) == False

assert serial_number.serial_old('123.124.123')
assert serial_number.serial_with_list_comprehension('123.124.123')


from arrays import *
assert rotate_array.rotate_array([1, 2, 3, 4], 2) == [3, 4, 1, 2]


# :) 
import this