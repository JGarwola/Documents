import numpy as np
import numba as nb
from Calc_kin_en import Ekin


@nb.njit
def lambda_coof(R,mass,N,T_0,dt,stdW=0.1,tau=1e-3):
    """
    Computes the lambda value used in cannonical sampling
    Coeficient for the update of the velocities
    """

    ekin,T   = Ekin(R,mass,N)
    dW       = np.random.normal(0,stdW)


    #lam = ( np.abs(1-(dt/tau)*(1- T_0/T)) )**(1/2) + ( np.abs(1+dW*(4*T_0/(3*T*tau))**(1/2)) )**(1/2)
    lam = ( np.abs(1 - (dt/tau)*(1-T_0/T) + dW*(4*T_0/(3*N*T*tau))**(1/2)) )**(1/2)

    return lam,ekin # the kinetic energy is given for free
