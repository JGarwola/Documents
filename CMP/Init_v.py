import numpy as np

def Init_v(R,mass):
    """
    Set all initial velocities in a way such that CM to have zero momentum
    """
    p     = ( R[:,1].T * mass.T ).T 
    p_tot = np.sum( p , axis = 0 )
    m_tot = np.sum(mass)
    R[:,1] -= p_tot / m_tot
    return R

