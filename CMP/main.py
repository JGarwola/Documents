import numpy as np
import numba as nb
import matplotlib.pyplot as plt

from Init_masses_arr import Init_masses_arr
from Init_potential_parameters_arr import Init_pot_par
from Init_v import Init_v
from Init_pos import Lattice_R0,Line_R0

from step import step


#--- Run parameters
nst = 1000 #number of steps
dt  = 0.001 #time step size
tau = 0.001 # lamb parameter
stdW = 0.1 # lamb parameter
L   = 5 #size of the box
N   = 3 #number of partickles
M   = 2 #number of types of partickles
reset_p_tot = N/100 #how often set total momentum to zero

# cut_off for things not to go nuts
cut_off_f = np.nan
cut_off_d = 0.0



T_0   = 1e-4#initial temperature
k     = 1.0 #Boltzman constant
types = np.array(np.random.randint(2,size=N)) # randomly choose the type of the particles

epsilon_diag = np.array([1,1]) #energy for LJ potencial
sigma_diag   = np.array([1,1]) #characterstic distances
disp         = 0.3 #displacement from lattice in initial posiations
mass_diag    = np.array([1.5,1]) #mass of each type


mass          = Init_masses_arr(mass_diag,types) # Array (1xN) with the masses
epsilon,sigma = Init_pot_par(epsilon_diag,sigma_diag) # Matrices with the cross terms of the coupling parameters in the potential


# Initial configuration
R_0      = np.random.uniform(0,L,(N,3,3)) # (N, variable, dimension)
R_0[:,1] = np.random.uniform(-1,1,size=(N,3))*0.1
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


colors = ['b','r']
fig    = plt.figure()
ax     = fig.add_subplot(111, projection='3d')
jumps  = 50

for i in range(N):
    ax.scatter( data_conf[ ::jumps , i , 0 , 0 ] ,
                data_conf[ ::jumps , i , 0 , 1 ],
                data_conf[ ::jumps , i , 0 , 2 ]
                  )


ax2 = fig.add_subplot(444)
ax2.plot( data_en[:,0] , label = r'$E_{potential}$' )
ax2.plot( data_en[:,1] , label = r'$E_{kinetic}$' )
ax2.plot( data_en[:,0]+data_en[:,1] , label = r'$E_{tot}$' )
plt.show()
