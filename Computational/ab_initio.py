m = 1.0 #mass
nst = 100 #number of spets
dt = 0.00001 #time step size
k = 1.0 #Boltzman constant
T = 1.0 #initial temperature
N = 5 #number of partickles
L = 5 #size of the box
epsilon = 1.0 #parameter for LJ potencial
disp = 0.1 #displacement from lattice in initial posiations
sigma = k*T/m

import numpy as np
from numpy import linalg as la
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

def modL(r):
    return r%L

def dist(R,i,j):
    return R[i,0]-R[j,0]

def temp(R, i, eta = 1, N = 1):
    Ekin = 0.0
    for i in range(np.shape(R)[i,0]-1):
        Ekin += m*la.norm(R[i,1])**2
    return (Ekin)/(eta*N*k)

def force(d):
    sigma = 1.0
    return -4*epsilon*( 12*((sigma/la.norm(d))**12) -
                        6*((sigma/la.norm(d))**6) )*d/la.norm(d)
    #return 1/dist**2

def calc_energy(R):
    Epot = np.empty(N)
    Ekin = np.empty(N)
    resault = np.empty((N,2))
    for i in range(N-1):
        Epot[i] = 0.0
        for j in range(N-1):
            d = dist(R,i,j)
            if( (i!=j) ):
                Epot[i] += -4*epsilon*( ((sigma/la.norm(d))**12)
                                        - ((sigma/la.norm(d))**6) )
        Ekin[i] = m*la.norm(R[i,1])**2/2
    return np.transpose(np.array([Ekin,Epot]))

def step(R):
    Rp = np.zeros(np.shape(R_0))
    for i in range(N):
        F_old = R[i,2]
        F = np.zeros(3)
        for j in range(N):
            d = dist(R,i,j)
            if( (i!=j) ):
                F += force(d)
        v = R[i,1] + (F + F_old)*dt/2*m
        r = R[i,0] + R[i,1]*dt + F*(dt**2)/(2*m)
        Rp[i] = np.array([modL(r),v,F])
    return Rp

R_0 = np.random.normal(L/2,L/2,(N,3,3)) # (N, variable, dimension)
R_0[:,1] *= 0.0
R_0[:,0] = np.reshape(np.linspace(0,L,N*3,endpoint=0)
                        + np.random.normal(0.0,disp,N*3),(5,3))

data = np.empty((nst,N,3,3)) # data([step, partickle, variable, dim])
data[0] = R_0
ens = np.empty((nst,N,2)) # energies([step, partickle, [kin,pot] ])
ens[0] = calc_energy(R_0)

for i in range(1,nst): #1 not to use random bites form empty
    input = data[i-1]
    output = step(input)
    data[i] = output
    ens[i] = calc_energy(output)

#np.savetxt("data.txt", np.reshape(data,(nst*N,3)))

#fig,ax = plt.subplots(2)
#ax[0].plot(data[:,0,0,1:])
#ax[1].plot(range(nst),np.sum(ens[:,:,1]+ens[:,:,0],axis=1))


fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.plot3D(data[:,0,0,0], data[:,0,0,1], data[:,0,0,2])
ax.plot3D(data[:,1,0,0], data[:,1,0,1], data[:,1,0,2])
ax.set_title('orbit if 0th partickle')

plt.show()
