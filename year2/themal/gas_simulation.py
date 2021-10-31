#! python3
# print('Shalom 2nd year')
# import tools (that makes it look like you have MATLAB)
import numpy as np  # the power of vectors and matrices
import matplotlib.pyplot as plt  # the power of graphs
from matplotlib.patches import Circle
import random  # random number generators

# vector = np.array([1, 2, 3, 4, 5])
# fine_vector = np.linspace(1, 5, 1000)
# plt.figure('test')
# plt.clf()  # clear figure
# plt.plot(vector, vector**2, 'or')
# plt.plot(fine_vector, 1.0*fine_vector**2, 'b')
# plt.show()

# define a function that moves particles one step
def move(i, gas, N, L, hits, m):
    for n in range(N):
        c = gas[n]
        currentx, currenty = c.center
        if (currentx + c.vx > L) or (currentx + c.vx < 0):
            if (currentx + c.vx > L):
                # if we hit the right wall: add the momentum kick
                hits.append(2*m*c.vx)
            c.vx = -c.vx
        if (currenty + c.vy > 1) or (currenty + c.vy < 0):
            c.vy = -c.vy
        c.center = currentx+c.vx, currenty+c.vy

def run_sim(L):
    # Build a world
    plt.figure('Our first world')
    plt.clf()
    plt.gca().set_aspect('equal')
    V = L*1  # two-dimensional volume
    plt.plot(np.array([0, L, L, 0, 0]), np.array([0, 0, 1, 1, 0]), 'k')
    plt.plot(np.array([L, L]), np.array([0, 1]), color='orange')
    plt.title(f'A model of a piston Volume = {V}')
    # add molecules of gas
    r = 0.01  # radius of a molecule
    N = 150  # number of gas molecules
    m = 1  # mass of a single molecule
    v = 0.01  # absolute value of velocity
    gas = []  # a list of gas molecules
    for n in range(N):
        # choose a random location of the particles (but leave a 2r
        # margin on each side
        xstart = random.random()*(L-4*r) + 2*r
        ystart = random.random()*(1-4*r) + 2*r
        c = Circle((xstart, ystart), r, color='blue')
        plt.gca().add_patch(c)
        # all particles have the same v but different directions
        theta = random.random() * 2 * np.pi
        c.vx = v*np.cos(theta)
        c.vy = v*np.sin(theta)
        gas.append(c)

    # now iterate
    i = 0  # descrete time (start at t=0)
    max_iterations = 5000  # end of time

    hits = []  #list of coliisions on the right wall
    while (i < max_iterations):
        move(i, gas, N, L, hits, m)
        # plt.pause(0.001)  # add a little pause to update monitor
                          # but if you want a faster simulation, comment
                          # this out
        i += 1  # time moves forward
    # now calculate Pressure
    area = 1
    P = np.sum(hits)/max_iterations/area
    return V, P


Vs = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

res = {}

# for i in Vs:
#     for _ in range(10):
#         V, P = run_sim(i)
#         if V in res.keys():
#             res[V].append(P)
#         else:
#             res[V] = [P]
#     print(res)
res = {1.0: [0.007905468864272968, 0.007052589893660522, 0.007869316170723666, 0.007575045062022681, 0.007247131622944769, 0.008080527090809277, 0.008433339581270884, 0.00718366161124829, 0.007809597225488438, 0.008087019332800182], 2.0: [0.003643825838752741, 0.003561090234033857, 0.0037801521592661274, 0.003887904179090605, 0.0038936888489099304, 0.003905572387404799, 0.004150933804587388, 0.003814765886519568, 0.0036701368375325373, 0.003605391501924579], 3.0: [0.00220942261087175, 0.0022703176684239932, 0.0024717177965493642, 0.002487637756196419, 0.0023211481366870613, 0.0024271844968352025, 0.002650696023843058, 0.0025651196773311077, 0.002707215206750615, 0.002674013579089797], 4.0: [0.0019079873963302326, 0.0018166600376933622, 0.0018702321737634443, 0.0018225515539998162, 0.001719014703385055, 0.001852432622828323, 0.0019236792111020239, 0.0018010109541202039, 0.0019312438144023368, 0.0019698358520926084], 5.0: [0.0015701671959223353, 0.0016523779453762246, 0.0015077562160762865, 0.001344631168434275, 0.0015990491052014415, 0.001531699011670457, 0.0014750026897384868, 0.0015106919378859393, 0.0014609315848281553, 0.0015280801595331291], 6.0: [0.0012178738517364613, 0.0012140586370794001, 0.001251897926715992, 0.0012158119574706546, 0.001341677596426052, 0.0014755746869002865, 0.0013477247279045437, 0.001317796908238347, 0.0012895001041283386, 0.001227012465257408], 7.0: [0.0009492049736234925, 0.000998146881184753, 0.000971826613497651, 0.0010040833868240426, 0.0011020232182317423, 0.001134390991626214, 0.0009791130422664171, 0.0011525981293428883, 0.0010763751870753184, 0.00099699658936288], 8.0: [0.0008677119497365179, 0.0009797899741913008, 0.0009734216428988617, 0.000922670638773927, 0.0008728020775962433, 0.0009145165679493527, 0.0010268280260533576, 0.0009938582015419696, 0.0008940509690271558, 0.0009973923822580676], 9.0: [0.0008540923279905838, 0.0009638087958103271, 0.0007996145064861223, 0.000877047574711791, 0.0008457637774629401, 0.0009211292554682028, 0.0008063533119669279, 0.000901941426732026, 0.0007363154140440136, 0.0008767725453523162], 10.0: [0.0007487432716528115, 0.0007037206173966766, 0.000781451345748995, 0.000802509277346556, 0.0007082309899450508, 0.0008845506545219775, 0.000772503759168013, 0.0007897092884404334, 0.0007523866957480916, 0.000750678770055236]}

const = []
for v in res.keys():
    P = np.mean(res[v])
    dp = np.std(res[v])
    plt.errorbar(v, P, yerr=dp, fmt='o')
    const.append(P*v)

print("const: ", np.mean(const))

x = np.linspace(1, 10, 500)
y = np.mean(const) / x

plt.plot(x, y)
plt.xlabel('V')
plt.ylabel('P')
plt.title('P vs V')
plt.legend(["PV=const"])

plt.show()

# now to summarize
# plt.figure('P vs V')
# plt.plot(V, P, 'o', color='magenta')
# plt.xlabel('V')
# plt.ylabel('P')
# plt.show()
