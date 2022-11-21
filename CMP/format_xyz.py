import numpy as np
from parameters import *

def form(types, data, labels):
    f = open("data.xyz", "w")
    for i in range(nst):
        #f.write("{}\n i={}, time = {}\n".format(N,i,i*dt))
        f.write("{}\nFrame {}\n".format(N,i))
        for j in range(N):
            f.write("{} {} {} {}\n".format(labels[types[j]],data[i,j,0,0],
                                data[i,j,0,1],data[i,j,0,2]))
    f.close()
