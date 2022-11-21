
import numpy as np
from numpy import linalg as la
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
import numba as nb

mases = np.array([1,2]) #mass of each type
nst = 5000 #number of spets
dt = 0.001 #time step size
k = 1.0 #Boltzman constant
T_0 = 1e-6 #initial temperature
N = 120 #number of partickles
types = np.array(np.random.randint(2,size=N))
M = 2 #number of types of partickles
L = 20 #size of the box
epsilon_diag = np.array([1,2]) #energy for LJ potencial
sigma_diag = np.array([1,2]) #characterstic distances
disp = 0.5 #displacement from lattice in initial posiations

epsilon = np.empty((M,M))
sigma = np.empty((M,M))
for i in range(M):
    for j in range(M):
        epsilon[i,j] = (epsilon_diag[i]*epsilon_diag[j])**(1/2)
        sigma[i,j] = (sigma_diag[i]+sigma_diag[j])/2
mases2 = np.zeros(N)
for i in range(N):
    mases2[i] = mases[types[i]]

@nb.njit
def modL(r):
    return r%L

@nb.njit
def dist(R,i,j):
    d = R[i,0]-R[j,0]
    if(d@d < (0.5)**2):
        d =  0.5*d/la.norm(d)
    return d

@nb.njit
def force(d,i,j):
    dot = d@d
    f = -4*epsilon[i,j]*( 12*((sigma[i,j]**2/dot)**6) -
                        6*((sigma[i,j]**2/dot)**3) )*d/dot
    if(f@f > 25):
        f = 5*f/la.norm(f)
    return f

#@nb.njit
def calc_energy(R,types,mases):
    Epot = np.zeros(N)
    Ekin = np.empty(N)
    resault = np.empty((N,2))
    for i in range(N-1):
        for j in range(i+1,N):
            d = dist(R,i,j)
            dot = d@d
            Epot[i] += -4*epsilon[types[i],types[j]]*(
                        ((sigma[types[i],types[j]]**2/dot)**6)
                        - ((sigma[types[i],types[j]]**2/dot)**3) )
            Epot[j] += Epot[i]
        Ekin[i] = mases[types[i]]*R[i,1]@R[i,1]/2
    return np.transpose(np.array([Ekin,Epot]))

#@nb.njit
def step2(R,types,mases):
    Rp = np.zeros(np.shape(R))
    F = np.zeros((N,3))
    for i in range(N):
        for j in range(i+1,N):
            f = force(dist(R,i,j),types[i],types[j])
            F[i] += f
            F[j] -= f
    m = np.transpose(np.array([mases[types[:]],mases[types[:]],mases[types[:]]]))
    v = R[:,1] + (F[:] + R[:,2])*dt/2*m
    v = lambda_coof(R)*v
    r = R[:,0] + R[:,1]*dt + F[:]*(dt**2)/(2*m)
    Rp = np.transpose(np.array([modL(r),v,F]), (1,0,2) )
    return Rp

def zero_tot_p(R,types):
    p_tot = np.zeros(3)
    for i in range(N):
        p_tot += mases[types[i]]*R[i,1]
    for i in range(N):
        R[i,1] -= p_tot/(np.sum(mases))
    return R

def step(R):
    Rp = np.zeros(np.shape(R_0))
    for i in range(N):
        F_old = R[i,2]
        F = np.zeros(3)
        for j in range(i,N):
            d = dist(R,i,j)
            if( (i!=j) ):
                F += force(d)
        v = R[i,1] + (F + F_old)*dt/2*m
        r = R[i,0] + R[i,1]*dt + F*(dt**2)/(2*m)
        Rp[i] = np.array([modL(r),v,F])
    return Rp

def temp(R):
    Ekin = 0.0
    for i in range(N):
        Ekin += mases[types[i]]*R[i,1]@R[i,1]/2
    return (Ekin)/(3*N*k)

def lambda_coof(R):
    tau = 1e-3
    T = temp(R)
    print('temp = ',T)
    dW = np.random.normal(0,0.1)
    lam = ( abs(1-(dt/tau)*(1- T_0/T)) )**(1/2) +\
            ( abs(1+dW*(4*T_0/(3*T*tau))**(1/2)) )**(1/2)
    print('lambda = ',lam)
    return lam

R_0 = np.random.uniform(0,L,(N,3,3)) # (N, variable, dimension)
R_0[:,1] = np.random.uniform(-1,1,size=(N,3))
R_0 = zero_tot_p(R_0,types)

data = np.empty((nst,N,3,3)) # data([step, partickle, variable, dim])
data[0] = R_0
ens = np.empty((nst,N,2)) # energies([step, partickle, [kin,pot] ])
ens[0] = calc_energy(R_0,types,mases)

for i in range(1,nst): #1 not to use random bites form empty
    input = data[i-1]
    output = step2(input,types,mases)
    data[i] = output
    ens[i] = calc_energy(output,types,mases)

#np.savetxt("data.txt", np.reshape(data,(nst*N,3)))

colors = ['b','r']
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(N):
    ax.scatter(data[::50,i,0,0], data[::50,i,0,1],
                data[::50,i,0,2], c=colors[types[i]])
ax2 = fig.add_subplot(444)
ax2.plot(range(nst),np.sum(ens[:,:,1]+ens[:,:,0],axis=1))
plt.show()
