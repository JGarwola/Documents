m = 1.0 #mass
nst = 100 #number of spets
dt = 0.0001 #time step size
k = 1.0 #Boltzman constant
T = 1.0 #initial temperature
N = 3 #number of partickles
L = 10 #size of the box
epsilon = 1.0 #parameter for LJ potencial
sigma = k*T/m

import numpy as np
from matplotlib import pyplot as plt

def modL(r):
    return r%L

def dist(R,i,j):
    return R[i,0]-R[j,0]

def temp(R, i, eta = 1, N = 1):
    Ekin = 0.0
    for i in range(np.shape(R)[i,0]-1):
        Ekin += m*R[i,1]**2
    return (Ekin)/(eta*N*k)

def force(R,i,j):
    sigma = 1.0
    d = dist(R,i,j)
    return -4*epsilon*( 12*((sigma/d)**12) - 6*((sigma/d)**6) )/d
    #return 1/dist**2

def calc_energy(R):
    Epot = np.empty(N)
    Ekin = np.empty(N)
    for i in range(N-1):
        Epot[i] = 0.0
        for j in range(N-1):
            if(i != j):
                d = dist(R_0,i,j)
                Epot[i] += -4*epsilon*( ((sigma/d)**12) - ((sigma/d)**6) )
        Ekin[i] = m*R_0[i,1]**2/2
    return np.reshape(np.array([Ekin,Epot]),(3,2))

def step(R):
    Rp = np.zeros(np.shape(R_0))
    for i in range(N-1):
        F_old = R[i,2]
        F = 0.0
        for j in range(N-1):
            if(j != i):
                F += force(R,i,j)
        v = R[i,1] + (F + F_old)*dt/2*m
        r = R[i,0] + R[i,1]*dt + F*(dt**2)/(2*m)
        Rp[i] = np.array([modL(r),v,F])
    return Rp

R_0 = np.array([np.random.normal(0.0,1.0),np.random.normal(0.0,sigma),0])
for i in range(N-1):
    R_0 = np.vstack((R_0,[[np.random.normal(0.0,1.0),
                        np.random.normal(0.0,sigma),0]]))

data = np.empty((nst,N,3)) # data([step, partickle, variable])
data[0] = R_0
ens = np.empty((nst,N,2)) # energies([step, partickle, [kin,pot] ])
ens[0] = calc_energy(R_0) # check if reshape makes sense

for i in range(1,nst): #1 not to use random bites form empty
    input = data[i-1]
    output = step(input)
    data[i] = output
    ens[i] = calc_energy(output)

np.savetxt("data.txt", np.reshape(data,(nst*N,3)))

fig,ax = plt.subplots(2)
ax[0].plot(range(nst),data[:,:,0])
ax[1].plot(range(nst),ens[:,:,1])
plt.show()
