import numpy as np 
import numba as nb
from Force_n_V import force_n_V
from Dist import dist

@nb.njit
def ForceV(R,types,mass,N,epsilon,sigma,L, cut_off_f , cut_off_d):
    """
    Computes the full force vector and the whole potential energy
    """

    F = np.zeros((N,3))
    V = 0
    for i in range(N):
        for j in range(i+1,N):

            d = dist(R,i,j,L,cut_off=cut_off_d)

            f,v   = force_n_V( d
                                    ,i,j,epsilon,sigma, types = types
                                    ,cut_off = cut_off_f   )
                                    
            F[i] += f
            F[j] -= f # third law 
            V    += 2 * v

    return F,V