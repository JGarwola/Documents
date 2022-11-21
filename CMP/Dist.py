import numpy as np
import numba as nb
import numpy.linalg as la


@nb.njit
def dist(R,i,j,L,cut_off=0.5):
    """
    Computes the distance between i and j particle
    """
    d = (R[j,0] -  R[i,0])
    d = np.sign(d) * (np.abs(d)%L) # correct way to implement the contribution of pbc

    # the problem was solved, this part may be removed in the future for optimization reasons
    n = la.norm(d)

    if  n < cut_off :
        d /= n * cut_off

    return d
