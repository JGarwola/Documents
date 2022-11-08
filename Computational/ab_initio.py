m = 1.0 #mass
nst = 10000 #number of spets
dt = 0.0001 #time step size
k = 1.0 #Boltzman constant
T = 1.0 #initial temperature
N = 3 #number of partickles
L = 10 #size of the boxx

import numpy as np
from matplotlib import pyplot as plt

sigma = k*T/m

def modL(r):
    return r%L

R_0 = np.array([np.random.normal(0.0,1.0),np.random.normal(0.0,sigma),0])
for i in range(N-1):
    R_0 = np.vstack((R_0,[[np.random.normal(0.0,1.0),
                        np.random.normal(0.0,sigma),0]]))

def temp(R, i, eta = 1, N = 1):
    Ekin = 0.0
    for i in range(np.shape(R)[i,0]-1):
        Ekin += m*R[i,1]**2
    return (Ekin)/(eta*N*k)

def force(R,i,j):
    sigma = 1.0
    epsilon = 1.0
    dist = R[i,0]-R[j,0]
    return -4*epsilon*( 12*((sigma/dist)**12) - 6*((sigma/dist)**6) )/dist
    #return 1/dist**2

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

# data([step, partickle, variable])
data = np.empty((nst,N,3))
data[0] = R_0
#etot = np.array([])

for i in range(1,nst): #1 not to use random bites form empty
    input = data[i-1]
    output = step(input)
    data[i] = output
    #etot = np.append(etot, input[0]**2/2 + m/2*input[1]**2)

np.savetxt("data.txt", np.reshape(data,(nst*N,3)))

fig,ax = plt.subplots(2)
ax[0].plot(range(nst),data[:,:,0])
#ax[1].plot(range(nst),etot)
plt.show()
