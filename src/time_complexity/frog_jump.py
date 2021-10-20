"""
    Count minimal number of jumps from position X to Y.

    A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

    Count the minimal number of jumps that the small frog must perform to reach its target
"""
import math

def frog_jump(x, y, d):
    return math.ceil( (y-x)/d )
