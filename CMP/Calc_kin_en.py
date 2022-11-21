import numpy  as np
import numba as nb


@nb.njit
def Ekin(R,mass, N, k = 1 ):
    """
    Computes the kinetic energy with vector op
    """
    v    = R[:,1]
    p    = v.T * mass.T
    ekin = np.sum( v * p.T ) * 0.5
    return ekin , ekin / ( 3 * N * k )