import numpy as np
import numba as nb
from Full_Force import ForceV
from Lamb import lambda_coof
from PBC import modL
from Init_potential_parameters_arr import Init_pot_par


@nb.njit
def step(R,mass,dt,types,N,epsilon,sigma,L,T_0,tau=1.0e-3,stdW = 0.1,cut_off_d=0.5,cut_off_f=5):
    """
    Makes one step in our phase space
    ---
    R         : phase space point + forces (array (#particles,Components=3,dimension=3)
    mass      : array with the masses (array (Nx1))
    dt        : time step
    types     : array with the labels of the types of particles (Nx1)
    N         : # particles
    epsilon   : matrix with the coupling terms in the potential (MxM)
    sigma     : like epsilon
    L         : size of the box in one direction
    T_0       : temperature we want to fix
    tau       : parameter for cannonical sampling (fine tunning only)
    stdW      : random factor in the cannonical sampling (fine tunning only)
    cut_off_d : cut off on the minimum distance particles can be
    cut_off_f : maximum force particles can feel
    """

    F,V      = ForceV( R , types , mass , N , epsilon , sigma , L , cut_off_d = cut_off_d , cut_off_f = cut_off_f )
    v        = R[:,1] + ( ( F + R[:,2] ).T * dt / 2 / mass.T ).T

    lam,ekin = lambda_coof(R,mass,N,T_0,dt,tau=tau,stdW=stdW)
    v       *= lam
    r        = R[:,0] + v*dt + ( F.T*( dt ** 2 ) / ( 2 * mass.T ) ).T

    #R[:,0] = modL(r,L)
    R[:,0] = r
    R[:,1] = v
    R[:,2] = F

    return R, ekin , V

#N   = 20
#L   = 20
#R_0 = np.random.uniform(0,L,(N,3,3)) # (N, variable, dimension)
#types = np.random.randint(0,2,size=N)
#sig,eps = np.ones(N),np.ones(N)
#epsilon,sigma = Init_pot_par(eps,sig)
#mass          = np.random.random_sample(N)
#dt = 0.0001
#T_0 = 0.0001
#print( step(R_0,mass,dt,types,N,epsilon,sigma,L,T_0))
