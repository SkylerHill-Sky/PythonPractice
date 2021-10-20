from src.other.is_prime import *
from src.other.serial_number import *


def test_is_prime():
    assert is_prime(1230987623144987) == False

def test_serial_number():
    assert serial_old('123.124.123')
    assert serial_with_list_comprehension('123.124.123')

def test_all_other():
    test_is_prime()

test_all_other()