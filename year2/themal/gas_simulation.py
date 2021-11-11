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
def move(i, gas, N, L, hits_r, hits_l, hits_u, hits_d, m):
    for n in range(N):
        c = gas[n]
        currentx, currenty = c.center
        if (currentx + c.vx > L) or (currentx + c.vx < 0):
            if (currentx + c.vx > L):
                # if we hit the right wall: add the momentum kick
                hits_r.append(2*m*c.vx)
            if (currentx + c.vx < 0):
                # if we hit the left wall: add the momentum kick
                hits_l.append(2*m*c.vx)
            c.vx = -c.vx
        if (currenty + c.vy > 1) or (currenty + c.vy < 0):
            if (currenty + c.vy > 1):
                # if we hit the up wall: add the momentum kick
                hits_u.append(2*m*c.vy)
            if (currenty + c.vy < 0):
                # if we hit the down wall: add the momentum kick
                hits_d.append(2*m*c.vy)
            c.vy = -c.vy
        c.center = currentx+c.vx, currenty+c.vy

def run_sim(L, N, m, v):
    # Build a world
    # plt.figure('Our first world')
    # plt.clf()
    # plt.gca().set_aspect('equal')
    V = L*1  # two-dimensional volume
    # plt.plot(np.array([0, L, L, 0, 0]), np.array([0, 0, 1, 1, 0]), 'k')
    # plt.plot(np.array([L, L]), np.array([1, 0]), color='orange')
    # plt.plot(np.array([0, 0]), np.array([0, 1]), color='red')
    # plt.plot(np.array([0, L]), np.array([0, 0]), color='green')
    # plt.plot(np.array([0, L]), np.array([1, 1]), color='orange')
    # plt.title(f'A model of a piston Volume = {V}')
    # add molecules of gas
    r = 0.01  # radius of a molecule
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

    hits_r = []  #list of coliisions on the right wall
    hits_l = []
    hits_u = []
    hits_d = []
    while (i < max_iterations):
        move(i, gas, N, L, hits_r, hits_l, hits_u, hits_d, m)
        plt.pause(0.001)  # add a little pause to update monitor
                          # but if you want a faster simulation, comment
                          # this out
        i += 1  # time moves forward

    # print(np.sum(hits_u), np.sum(hits_d), np.sum(hits_l), np.sum(hits_r))
    # now calculate Pressure
    length = L
    width = 1
    P_r = np.sum(hits_r) / max_iterations / width
    P_l = np.sum(hits_l) / max_iterations / width
    P_u = np.sum(hits_u) / max_iterations / length
    P_d = np.sum(hits_d) / max_iterations / length

    # plt.plot()

    return V, P_r, P_l, P_u, P_d

def s2():
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

def s3():
    res = {'r':[], 'u':[], 'd':[], 'l':[]}
    for _ in range(10):
        V, P_r, P_l, P_u, P_d = run_sim(2)
        res['r'].append(P_r)
        res['u'].append(P_u)
        res['d'].append(P_d)
        res['l'].append(P_l)

    P_r = abs(np.mean(res['r']))
    P_l = abs(np.mean(res['l']))
    P_u = abs(np.mean(res['u']))
    P_d = abs(np.mean(res['d']))

    print("Pressure on right wall {}\n"
          "Pressure on left wall {}\n"
          "Pressure on upper wall {}\n"
          "Pressure on bottom wall {}".format(str(P_r), str(P_l), str(P_u), str(P_d)))

def s3b():
    res = {0.002521720522661402: 50,
            0.005042967581253781: 100,
            0.007564375349989518: 150,
            0.010084975791398467: 200,
            0.01260621061501792: 250,
            0.015128401653329529: 300,
            0.017649998336445: 350,
            0.020168387193811067: 400,
            0.02268493919532535: 450,
            0.025212499691009575: 500}
    # N = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    # for n in N:
    #     res = {'r': [], 'u': [], 'd': [], 'l': []}
    #     for _ in range(10):
    #         V, P_r, P_l, P_u, P_d = run_sim(1, n, 1, 0.01)
    #         res['r'].append(P_r)
    #         res['u'].append(P_u)
    #         res['d'].append(P_d)
    #         res['l'].append(P_l)
    #
    #     P_r = abs(np.mean(res['r']))
    #     P_l = abs(np.mean(res['l']))
    #     P_u = abs(np.mean(res['u']))
    #     P_d = abs(np.mean(res['d']))
    #     P = np.mean([P_r, P_l, P_u, P_d])

    x_1 = list(res.values())
    y_1 = list(res.keys())
    m = (y_1[-1] - y_1[0]) / (x_1[-1] - x_1[0])
    x = np.linspace(min(x_1), max(x_1), 100)

    y = m*x
    print(m)
    plt.plot(x_1, y_1, 'o')
    plt.plot(x, y)
    plt.grid()
    plt.xlabel("N [number of molecule]")
    plt.ylabel("P [pressure]")
    plt.title("P(N) = Const\nconst = {}".format(str(m)))
    plt.show()

def s4():
    res = {0.007562161058513448:1,
           0.015125490651225322:2,
           0.022688096027486275: 3,
           0.030258039613829585: 4,
           0.037803829548286406: 5,
            0.04537605099912437:6,
            0.05295728164903268:7,
            0.06049879470404259:8,
            0.0680761285615923:9,
            0.07563437322434387:10}
    # M = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # for m in M:
    #     res = {'r': [], 'u': [], 'd': [], 'l': []}
    #     for _ in range(10):
    #         V, P_r, P_l, P_u, P_d = run_sim(1, 150, m, 0.01)
    #         res['r'].append(P_r)
    #         res['u'].append(P_u)
    #         res['d'].append(P_d)
    #         res['l'].append(P_l)
    #
    #     P_r = abs(np.mean(res['r']))
    #     P_l = abs(np.mean(res['l']))
    #     P_u = abs(np.mean(res['u']))
    #     P_d = abs(np.mean(res['d']))
    #     P = np.mean([P_r, P_l, P_u, P_d])
    #
    #     print(P, m)
    x_1 = list(res.values())
    y_1 = list(res.keys())
    m = (y_1[-1] - y_1[0]) / (x_1[-1] - x_1[0])
    x = np.linspace(min(x_1), max(x_1), 100)

    y = m*x
    print(m)
    plt.plot(x_1, y_1, 'o')
    plt.plot(x, y)
    plt.grid()
    plt.xlabel("m [mass of molecule]")
    plt.ylabel("P [pressure]")
    plt.title("P(m) = Const\nconst = {}".format(str(m)))
    plt.show()

def s5():
    res = {0.007567366961075095:0.01,
            0.0305136756320131:0.02,
            0.06924783485605052:0.03,
            0.12430173554991421:0.04,
            0.19585889297415782:0.05,
            0.2842393545891846:0.06,
            0.3915553370353595:0.07,
            0.5150221175208352:0.08,
            0.6575890730903173:0.09,
            0.8205799744493327:0.1}
    # V = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]
    # for v in V:
    #     res = {'r': [], 'u': [], 'd': [], 'l': []}
    #     for _ in range(10):
    #         V, P_r, P_l, P_u, P_d = run_sim(1, 150, 1, v)
    #         res['r'].append(P_r)
    #         res['u'].append(P_u)
    #         res['d'].append(P_d)
    #         res['l'].append(P_l)
    #
    #     P_r = abs(np.mean(res['r']))
    #     P_l = abs(np.mean(res['l']))
    #     P_u = abs(np.mean(res['u']))
    #     P_d = abs(np.mean(res['d']))
    #     P = np.mean([P_r, P_l, P_u, P_d])
    #
    #     print(P, v)
    #     plt.plot(v, P)
    # plt.show()
    x = res.values()
    y = res.keys()
    plt.plot(x, y, 'o')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    # run_sim(1, 150, 1, 0.01)
    s3b()
    # s4()
    # s5()
