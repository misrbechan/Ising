# preliminary initial lattice
import numpy as np
n = 2  # dimension lattice
J = 1
H = 1
E_J = 0
E_Jnew = 0
T = 1
kb = 1.38 *10**-23
beta = (kb*T)**-1

R = np.zeros((n,n)) + np.random.choice([-1,1],p=[0.5, 0.5]) #total system up/down with p=0.5
R_new = R + np.zeros((n,n))

x = np.random.randint(0,n,2)

R_new [x[0],x[1]] =  -1 * R_new[x[0],x[1]] # new lattice is old with one random spin flipped

for i in range (n):
    E_H = -H * np.sum(R)
    E_Hnew =  -H * np.sum(R_new)
    for j in range (n):
        E_J += -J * np.sum(R[i,j] * R)
        E_Jnew += -J * np.sum(R_new[i,j] * R_new)

E = beta * (E_J + E_H )
E_new = beta * (E_Jnew + E_Hnew )
dE = E_new - E

