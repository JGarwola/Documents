import numpy as np 
import numba as nb 
import numpy.linalg as la
import matplotlib.pyplot as plt 

@nb.njit
def force_n_V(d,i,j,epsilon,sigma,types, cut_off ):
    """
    Computes the force and potential associated to the interaction between i and j particles
    """

    # just save some calculations on variables to save time, since this function is called a lot 
    dot    = d@d 
    itype  = types[i]
    jtype  = types[j]
    idots3 = (sigma[itype,jtype]**2/dot) ** 3
    V6     = idots3
    V12    = idots3 * idots3  
    V      = 4 * epsilon[itype,jtype] * ( V12 - V6 ) 
    f      = -4 * epsilon[itype,jtype]* ( 12 * V12 - 6 * V6 ) * d / dot

    # the problem was solved 
    #n = la.norm(f)
    #if( n > cut_off ):
     #   f /= cut_off * n
        
    return f , V


