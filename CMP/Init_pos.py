import numpy  as np


def Lattice_R0(R,N,L,w=0):
    """
    Initialize the positions of the particles in a lattice
    """

    ## Note: this function still does not do the desired function, play around with the number of particles 
    # in the case of errors.
    n = int(N**(1/3)+1)
    x = np.linspace( 0.5 , L , n , endpoint = False)
    X,Y,Z = np.meshgrid(x,x,x) 
    A = np.array([X,Y,Z])
    A = np.transpose(A,(1,2,3,0)) 
    A = np.reshape( A, (n**3,3))
    R[:,0] = A[:N] + w * ( np.random.random_sample((N,3)) - 0.5 )
    return R

def Line_R0( R,N,L,w=0):
    """ 
    Put all particles in a line in x, good for testing
    """
    x = np.linspace( 0 , L , N , endpoint = False )
    Rn = np.zeros(( N , 3 ) )
    Rn[:,0] = x 
    R[:,0] = Rn
    return R
    
