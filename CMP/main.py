import numpy as np
import numba as nb
from parameters import *
from format_xyz import form

from Init_masses_arr import Init_masses_arr
from Init_potential_parameters_arr import Init_pot_par
from Init_v import Init_v
from Init_pos import Lattice_R0,Line_R0

from step import step

epsilon_diag = np.array([1,1]) #energy for LJ potencial
sigma_diag   = np.array([1,1]) #characterstic distances
disp         = 0.3 #displacement from lattice in initial posiations
mass_diag    = np.array([1.5,1]) #mass of each type


mass          = Init_masses_arr(mass_diag,types) # Array (1xN) with the masses
epsilon,sigma = Init_pot_par(epsilon_diag,sigma_diag) # Matrices with the cross terms of the coupling parameters in the potential


# Initial configuration
R_0      = np.random.uniform(0,L,(N,3,3)) # (N, variable, dimension)
R_0[:,1] = np.random.uniform(-1,1,size=(N,3))*0.5
R_0[:,2] = 0
R_0      = Init_v(R_0,mass) # set the total momentum to zero
#R_0      = Line_R0(R_0,N,L,w=0)
#R_0[:,0,0] = np.array([1+(2)**(1/6),1+0.1])
#R_0      = Lattice_R0(R_0,N,L,w=0)


# data
data_conf = np.zeros((nst,N,3,3))
data_en   = np.zeros((nst,2))

# main loop
j = 0
for i in range(nst):

    j += 1
    if(j == reset_p_tot):
        R_0 = Init_v(R_0, mass)
        j = 0

    data_conf[i] = R_0

    R_0,Ek,Ep    = step( R_0 , mass , dt
                        ,types , N , epsilon ,
                        sigma, L , T_0 , tau = tau , stdW = stdW,
                        cut_off_d=cut_off_d,
                        cut_off_f=cut_off_f ) # black magic happens here :o

    data_en[i]  = Ep,Ek

form(types, data_conf, labels)
np.savetxt("data_conf.xyz", np.reshape(data_conf[:,:,0,:],(nst,N*3)), header='configuration in simulation' )
np.savetxt("data_en.xyz", data_en, header='energies in simulation')
