import numba as nb
import numpy as np 


@nb.njit
def modL(r,L):
    """
    Set's pbc on vectors
    """
    return r%L