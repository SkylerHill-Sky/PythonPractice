from src.pythonic_ways.inheritance_pythonic import *

def test_inheritance_pythonic():
    a = Person('John', 'Doe')
    b = Person(last_name='Bobby', first_name='Ricky')
    c = Teenager('Boy', 'George', 2543667707, 'joehoward.com')
    d = Teenager(first_name='Jack', phone_number='1231231111', last_name='Black', website='google.com')
    # todo add assertions and more code in inheritance_python
    # print('\t'.join([str(a), str(b), str(c), str(d)]))
    # print('\t'.join([dict(a), dict(b), dict(c), d.__dict__]))

def test_all_pythonic_ways():
    test_inheritance_pythonic()

test_all_pythonic_ways()
