import numpy as np 


def Init_pot_par(eps,sig):
    """
    Initialize the matrices with the cross 
    terms of the coupling terms in the interaction
    """
    
    M       = len(eps)
    epsilon = np.empty((M,M))
    sigma   = np.empty((M,M))
    for i in range(M):
        for j in range(M):
            epsilon[i,j] = (eps[i]*eps[j])**(1/2)
            sigma[i,j]   = (eps[i]+eps[j])/2

    return epsilon,sigma