"""
    I know this isn't a pythonic way of running all tests
        - i'm coming back with more reorg revisions
        
    Note to self:
        might organize my tests into classes - not sure yet
        look into setting up unit test to be customized via commandline
"""

from test_counting_elements import test_all_counting_elements
from test_iterations_arrays import test_all_iterations_arrays
from test_other import test_all_other

def test_all_practices():
    test_all_counting_elements()
    test_all_iterations_arrays()
    test_all_other()

test_all_practices()
import this # :) 
