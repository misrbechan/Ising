# preliminary initial lattice
import numpy as np
n = 2  # dimension lattice
J = 1
H = 1
E_J = 0
T = 1
kb = 1.38 *10**-23
beta = (kb*T)**-1

R = np.zeros((n,n)) + np.random.choice([-1,1],p=[0.5, 0.5]) #total system up/down with p=0.5
for i in range (n):
    E_H = -H * np.sum(R)
    for j in range (n):
        E_J += -J * np.sum(R[i,j] * R)

E = beta * (E_J + E_H )
