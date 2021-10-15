import pytest
from IteratingParsing import BinaryGap
from IteratingParsing import isPrime
from IteratingParsing import SerialNumber

from Arrays import RotateArray
from Arrays import OddOccurences

assert BinaryGap.binary_gap(1000000000000000000000000020) == 22

assert isPrime.is_Prime(1230987623144987) == False

assert SerialNumber.serial_old('123.124.123')
assert SerialNumber.serial_with_list_comprehension('123.124.123')

assert RotateArray.rotate_array([1, 2, 3, 4], 2) == [3, 4, 1, 2]
