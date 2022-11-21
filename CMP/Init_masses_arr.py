import numpy as np 


def Init_masses_arr(mass,types):
    """
    Initialize the array (Nx1) with the value of the masses 
    """
    mass_arr = mass[types]
    return mass_arr


