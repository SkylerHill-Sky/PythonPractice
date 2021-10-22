"""
    I know this isn't a pythonic way of running all tests
        - i'm coming back with more reorg revisions
        
    Note to self:
        might organize my tests into classes - not sure yet
        look into setting up unit test to be customized via commandline
"""
import this # :) 

from test_counting_elements import test_all_counting_elements
from test_iterations_arrays import test_all_iterations_arrays
from test_other import test_all_other
from test_prefix_sums import test_all_prefix_sums
from test_pythonic_ways import test_all_pythonic_ways
from test_sorting import test_all_sorting
from test_stacks_queues import test_all_stacks_queues

def test_all_practices():
    test_all_counting_elements()
    test_all_iterations_arrays()
    test_all_other()
    test_all_prefix_sums()
    test_all_pythonic_ways()
    test_all_sorting()
    test_all_stacks_queues()
    

test_all_practices()
