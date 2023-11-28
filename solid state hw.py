import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import math
#1
a=2.464 #lattice constant
primitive_v1=np.array([
    [a*np.sqrt(3)/2],
    [1/2*a]
],dtype=np.float64)

primitive_v2=np.array([
    [a*np.sqrt(3)/2],
    [-1/2*a]
],dtype=np.float64)


a1x=primitive_v1[0][0]
a1y=primitive_v1[1][0]
a2x=primitive_v2[0][0]
a2y=primitive_v2[1][0]
b1x,b1y,b2x,b2y= symbols('b1x,b1y,b2x,b2y')
eq1 = Eq(a1x*b1x+a1y*b1y, 2*np.pi)
eq2 = Eq(a1x*b2x+a1y*b2y,0)
eq3=Eq(a2x*b1x+a2y*b1y,0)
eq4=Eq(a2x*b2x+a2y*b2y,2*np.pi)
sol = solve([eq1, eq2,eq3,eq4], [b1x,b1y,b2x,b2y])

reciprocal_v1=np.array([
    [sol[b1x]],
    [sol[b1y]]
])
reciprocal_v2=np.array([
    [sol[b2x]],
    [sol[b2y]]
])

print("b1="+str(reciprocal_v1))
print("b2="+str(reciprocal_v2))

#2
repeatition=10
a=2.464

reciprocal_vectors=np.array([
    [],
    []
])

for i in range(-repeatition,repeatition):
    for j in range(-repeatition,repeatition):
        reciprocal_vectors=np.hstack((reciprocal_vectors,i*reciprocal_v1+j*reciprocal_v2))

def reciprocal_draw():
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    plt.ylabel("K_y(1/Å)")
    plt.xlabel("K_x(1/Å)")
    plt.title("Reciprocal")
    plt.axis("equal")
    rx=reciprocal_vectors[0,:]
    ry=reciprocal_vectors[1,:]
    plt.plot(rx,ry,"o",color="r")

    def lines_draw(px,py):
        plt.plot([px+repeatition*py,px-repeatition*py],[py-repeatition*px,py+repeatition*px],color="grey")
    for i in range(0,reciprocal_vectors[0].size):
        lines_draw(0.5*reciprocal_vectors[0,i],0.5*reciprocal_vectors[1,i])

    plt.show()


reciprocal_draw()#原點放大後有六角形1st zone

#3
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
plt.title("E versus k")
epsilon=0
r=3
k_x=np.linspace(-1,1,1000)
k_y=np.linspace(-1,1,1000)
kx,ky=np.meshgrid(k_x,k_y)
E_plus=epsilon+r*np.sqrt(3+2*np.cos(np.sqrt(3)*ky*a)+4*np.cos(np.sqrt(3)*ky*a/2)*np.cos(3*kx*a/2))
E_minus=epsilon-r*np.sqrt(3+2*np.cos(np.sqrt(3)*ky*a)+4*np.cos(np.sqrt(3)*ky*a/2)*np.cos(3*kx*a/2))
ax.plot_surface(kx,ky,E_plus)
ax.plot_surface(kx,ky,E_minus)
ax.set_xlabel('kx')
ax.set_ylabel('ky')
ax.set_zlabel('E')
plt.show()