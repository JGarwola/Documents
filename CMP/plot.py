import matplotlib.pyplot as plt
from parameters import *
import numpy as np

data_conf = np.reshape(np.loadtxt("data_conf.xyz"),(nst,N,3))
data_en = np.reshape(np.loadtxt("data_en.xyz"),(nst,2))

colors = ['b','r']
fig    = plt.figure()
ax     = fig.add_subplot(111, projection='3d')
jumps  = 50

for i in range(N):
    ax.scatter( data_conf[ ::jumps , i , 0 ] ,
                data_conf[ ::jumps , i , 1 ],
                data_conf[ ::jumps , i , 2 ]
                  , c = colors[types[i]])


ax2 = fig.add_subplot(444)
ax2.plot( data_en[:,0] , label = r'$E_{potential}$', color="yellow" )
ax2.plot( data_en[:,1] , label = r'$E_{kinetic}$', color="red" )
ax2.plot( data_en[:,0]+data_en[:,1] , label = r'$E_{tot}$', color="blue" )
plt.show()
