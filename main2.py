import numpy as np
import random

def generarSintomas(us):
    for i in range(0,len(us[0])):
        us[0][i] = random.random()
    return us

def interseccionMatriz(mpc,mi,us):
    for i in range(0,mpc.shape[0]):
        for j in range(0,mpc.shape[1]):
            if mpc[i][j] >= us[0][j]:
                mi[i][j] = us[0][j]
            else:
                mi[i][j] = mpc[i][j]
    for i in range(0,mi.shape[0]):
        for j in range(0,mi.shape[1]-1):
            mi[i][15] += mi[i][j]
    return mi

mpc = [
    [ 0.5 , 0   , 0.9 , 0.8 , 0.8 , 0   , 0   , 0.6 , 0   , 0   , 0   , 0.4 , 0   , 0   , 0   ],
    [ 0.6 , 0   , 0   , 0   , 0.5 , 0.7 , 0   , 0   , 0   , 0   , 0   , 0   , 0.7 , 0   , 0   ],
    [ 0.9 , 0.3 , 0.8 , 0.8 , 0   , 0   , 0.5 , 0.6 , 0   , 0   , 0   , 0.7 , 0   , 0.5 , 0   ],
    [ 0.9 , 0.7 , 0.7 , 0   , 0   , 0   , 0.6 , 0.9 , 0   , 0   , 0   , 0   , 0   , 0   , 0   ],
    [ 0   , 0   , 0.9 , 0   , 0   , 0   , 0   , 0   , 0   , 0   , 0   , 0.9 , 0   , 0   , 0   ],
    [ 0   , 0   , 0.3 , 0   , 0.5 , 0   , 0   , 0   , 0   , 0   , 0.8 , 0.7 , 0   , 0   , 0   ],
    [ 0.4 , 0.7 , 0.9 , 0.6 , 0   , 0   , 0.6 , 0   , 0   , 0   , 0   , 0.3 , 0.5 , 0   , 0   ],
    [ 0.3 , 0   , 0.7 , 0.8 , 0   , 0   , 0.5 , 0   , 0   , 0   , 0.6 , 0.9 , 0   , 0   , 0.4 ],
    [ 0   , 0   , 0.8 , 0.7 , 0   , 0   , 0   , 0   , 0   , 0.7 , 0.5 , 0.6 , 0   , 0   , 0.6 ],
    [ 0   , 0   , 0.5 , 0.5 , 0.3 , 0   , 0.7 , 0   , 0.9 , 0.4 , 0.7 , 0.7 , 0   , 0.9 , 0   ]
]
mi = np.zeros((10,16),dtype=np.float64)
us = np.zeros((1,15),dtype=np.float64)
us = generarSintomas( us )
mi = interseccionMatriz(mpc,mi,us)