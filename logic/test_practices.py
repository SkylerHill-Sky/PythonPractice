import pytest
import binary_gap
import is_prime
import rotate_array
import serial_number

assert binary_gap.binary_gap(1000000000000000000000000020) == 22

assert is_prime.is_Prime(1230987623144987) == False

assert rotate_array.rotate_array([1, 2, 3, 4], 2) == [3, 4, 1, 2]

assert serial_number.serial_old('123.124.123')
assert serial_number.serial_with_list_comprehension('123.124.123')