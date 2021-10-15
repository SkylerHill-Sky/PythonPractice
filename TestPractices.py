import pytest
from Iterating import BinaryGap
from Iterating import isPrime
from Iterating import RotateArray
from Iterating import SerialNumber

assert BinaryGap.binary_gap(1000000000000000000000000020) == 22

assert isPrime.is_Prime(1230987623144987) == False

assert RotateArray.rotate_array([1, 2, 3, 4], 2) == [3, 4, 1, 2]

assert SerialNumber.serial_old('123.124.123')
assert SerialNumber.serial_with_list_comprehension('123.124.123')