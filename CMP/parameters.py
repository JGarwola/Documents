import numpy as np

#--- Run parameters
nst = 5000 #number of steps
dt  = 0.001 #time step size
tau = 0.001 # lamb parameter
stdW = 0.1 # lamb parameter
L   = 20 #size of the box
N   = 120 #number of partickles
M   = 2 #number of types of partickles
reset_p_tot = 50 #how often set total momentum to zero

# cut_off for things not to go nuts
cut_off_f = np.nan
cut_off_d = 0.0


types = np.array(np.random.randint(2,size=N)) # randomly choose the type of the particles
labels = ['A','B']
T_0   = 1#initial temperature
k     = 1.0 #Boltzman constant
