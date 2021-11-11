#! python3

# import tools (that makes it look like you have MATLAB)
import numpy as np  # the power of vectors and matrices
import matplotlib.pyplot as plt  # the power of graphs
from matplotlib.patches import Circle, Rectangle
import random  # random number generators
import sys  # for the progress bar
import numpy
import scipy.optimize as scimin
import matplotlib.pyplot as mpl
# define a progress bar
def update_progress(progress):
    barLength = 20 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\r{:2.0f}% |{}| {}".format(progress*100,'\u2588'*block + " "*(barLength-block),status)
    sys.stdout.write(text)
    sys.stdout.flush()


# Build a world
plt.figure('A harmonic piston')
plt.clf()
plt.gca().set_aspect('equal')
L = 2.0 #size of box along x
V = L*1 # two-dimensional volume
plt.plot(np.array([0,L,L,0,0]), np.array([0,0,1,1,0]), 'k')

# adding a harmonic oscillator
M = 1000 # mass
width = 0.1
omega0 = 2*np.pi/50
dt = 1 # time step for good measure
u_initial = -0.005 # initial velocity
wall = Rectangle((1-width/2,0),width, 1, color='orange')
plt.gca().add_patch(wall)
wall.u = u_initial

# add molecules of gas
r = 0.01 # radius of a molecule
N = 150# number of gas molecules
m = 1# mass of a single molecule
v = 0.005 # absolute value of velocity
gas = [] # a list of gas molecules
for n in range(N):
    # choose a random location of the particles (but leave a 2r
    # margin on each side
    xstart = (random.random()*(1-4*r-width/2) + 2*r)
    ystart = (random.random()*(1-4*r) + 2*r)
    c = Circle((xstart,ystart),r,color='blue')
    plt.gca().add_patch(c)
    # all particles have the same v but different directions
    #theta = random.random() * 2 * np.pi
    #c.vx = v*np.cos(theta)
    #c.vy = v*np.sin(theta)
    c.vx = v * np.random.normal()
    c.vy = v * np.random.normal()
    gas.append(c)
# print(np.std([c.vx for c in gas]))

# define a function that moves particles one step
def move(i):
    x_wall, y_wall = wall.xy
    x = x_wall
    # move the molecules
    for n in range(N):
        c = gas[n]
        currentx, currenty = c.center
        if (currentx + c.vx > x) or (currentx + c.vx < 0):
            if (currentx + c.vx > x):
                # if we hit the right wall: add the momentum kick
                hits.append(2*m*c.vx)
                vx_old = c.vx
                u_old = wall.u
                c.vx = - vx_old *(1-m/M)/(1+m/M)+2*u_old/(1+m/M)
                wall.u = u_old *(1-m/M)/(1+m/M) +2*(m/M)/(1+m/M)*vx_old
            else:    
                c.vx = -c.vx
        if (currenty + c.vy > 1) or (currenty + c.vy < 0):
            c.vy = -c.vy
        c.center = currentx+c.vx, currenty+c.vy
    # move the wall
    wall_x_list.append(x_wall)
    wall_u_list.append(wall.u)
    gas_vxsquared_list.append(np.mean([c.vx**2 for c in gas]))
    x_wall_new = x_wall + wall.u * dt
    u_wall_new = wall.u - omega0**2*(x_wall_new-(1-width/2))
    wall.xy = x_wall_new, y_wall
    wall.u = u_wall_new
   
# now iterate
i = 0 # descrete time (start at t=0)
max_iterations = 2000 # end of time
hits = [] #list of coliisions on the right wall
gas_vxsquared_list = []
wall_x_list = []
wall_u_list = []
show = False
while (i<max_iterations):
    move(i)
    if show:
        plt.pause(0.001) # add a little pause to update monitor
                     # but if you want a faster simulation, comment 
                     # this out
    else:
        update_progress(i/max_iterations)
    i=i+1 # time moves forward


def calc_sse(energy):
    f = np.zeros(len(energy))
    sse = energy
    for i in range(len(energy)):
        if sum(f[i]-energy[i]) < sum(sse):
           f[i] = sum((f[i] - energy[i])**2)


# in the end - what did we get
wall_u_list = np.array(wall_u_list)
#wall_x_list = np.array(wall_x_list)
# a numerical correction for wall_x_list
wall_x_list = np.array(wall_x_list +[wall_x_list[-1]])
wall_x_list = (wall_x_list[0:-1] +wall_x_list[1:])/2
gas_vxsquared_list = np.array(gas_vxsquared_list)
plt.figure('summary')
# plt.clf()
# plt.subplot(3, 1, 1)
# plt.plot(wall_x_list)
# plt.xlabel('time')
# plt.ylabel('x')
# plt.subplot(3,1,2)
# plt.plot(wall_u_list)
# plt.xlabel('time')
# plt.ylabel('u')
# plt.subplot(3, 1, 3)
wall_mechanical_energy = 0.5*M*wall_u_list**2 + 0.5*M*omega0**2*(wall_x_list-(1-width/2))**2

# with open(r"C:\Users\Chen\Desktop\test.csv", "w") as f:
#     f.write("\n".join([str(i) for i in wall_mechanical_energy]))
#


# y = (1/10)**(-x)
#
# plt.plot(x, y)
# gas_kinetic_energy = 0.5*m*gas_vxsquared_list*N
plt.plot((wall_mechanical_energy), label='wall')
x = np.linspace(0, 2000, 10**4)
mew = 2.9
lamda = mew / (2*M)
lamda_2 = mew / (2*M)
y = 0.012 * (np.e**(-lamda * x))


plt.plot(x, y, label='fit')

# plt.plot((gas_kinetic_energy),label='gas')
# plt.plot((wall_mechanical_energy + gas_kinetic_energy), label='wall+gas')
plt.legend()
ysc = plt.gca().get_ylim()
plt.ylim(0, ysc[1]*1.1)
plt.xlabel('time [sec]')
plt.ylabel('Energy [J]')
plt.tight_layout()
plt.grid()
plt.show()

