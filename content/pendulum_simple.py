import numpy as np
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from matplotlib import colors as mcolors
#import matplotlib.animation as animation


def pendrhs( z):
    ''' The right hand side of the pendulum equations `x'=f(x)` '''
    q = z[0]
    p = z[1]
    return np.array([ p, -np.sin(q)])

# Time stepping schemes

def stepEulerExplicit( xk, h) :
    '''Explicit Euler scheme'''
    return xk + h * pendrhs( xk)

def stepEulerImplicit( xk, h) :
    '''Implicit Euler scheme'''

    # start at an explicit Euler step for fast convergence
    xk_t1 = xk + h * pendrhs(xk)
    en = lambda x : xk + h*pendrhs(x) - x

    xk_t1, _, flag, msg = fsolve( func = en, x0 = xk_t1, full_output=True)
    if not flag == 1:
        print('Nonlinear solve encountered problem at t={0}: '.format(xk) + msg)

    return xk_t1

def stepEulerSymplectic( xk, h) :
    '''Symplectic Euler scheme'''
    dx = pendrhs( xk)
    p_t1 = xk[1] + h * dx[1]
    q_t1 = xk[0] + h * p_t1
    return np.array([q_t1, p_t1])

def stepRK4( xk, h) :
    '''Runge-Kutta-4'''
    k1 = h * pendrhs( xk)
    k2 = h * pendrhs( xk + k1 / 2.)
    k3 = h * pendrhs( xk + k2 / 2.)
    k4 = h * pendrhs( xk + k3)
    return xk + 1./6. * (k1 + 2.*k2 + 2.*k3 + k4)

# simulation loop

def simulate( infiniStep, inival, interval=[0, 1], Nts=100) :
    '''Run simulation / Finite time integrator'''

    t0, te = interval[0], interval[1]
    h = 1./Nts*(te-t0)
    N = inival.size

    sollist = [inival.reshape((1, N))]
    tlist = [t0]

    xk = inival

    for k in range(1, Nts+1):

        xk = infiniStep( xk, h)

        sollist.append( xk.reshape((1, N)))
        tlist.append( t0 + k*h)

    sollist = np.vstack( sollist)

    return sollist, tlist

##
# main

inival = np.array([ 0., 1.])
interval = [0, 50]
nSteps = 1000

# basic experiments
print( "Starting basic experiments.")

integrators = [stepEulerImplicit, stepEulerExplicit, stepRK4, stepEulerSymplectic]
integrator_labels = ['implicit Euler', 'explicit Euler', 'RK4', 'symplectic Euler']
sols = []

for integrator in integrators :
    sol, tlist = simulate( integrator, inival, interval, nSteps)
    sols.append( sol)

# long term integration
print( "Starting long term experiments.")

integrators_long = [stepEulerSymplectic, stepRK4, ]
integrator_labels_long = ['symplectic Euler', 'RK4']
sols_long = []

interval_long = [0, 1000*50]
nSteps_long = 300*1000
for integrator in integrators_long :
    sol, tlist = simulate( integrator, inival, interval_long, nSteps_long)
    sols_long.append( sol)

##
# plotting
colors = dict( mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

# space time plot

plt.figure(1)
for sol in sols :
    plt.plot( sol[:,0])
plt.xlabel('t'), plt.ylabel('x')
plt.legend( integrator_labels, loc=2)

# phase portrait

plt.figure(2)
for sol in sols :
    plt.plot( sol[:,0], sol[:,1])
plt.xlabel('x'), plt.ylabel('p')
plt.title( 'phase portrait')
plt.legend( integrator_labels, loc=2)

# energy

# the 1.0 = np.cos(0) is to account for that kinetic potential energy is
# maximal at the initial state and 0 at
plt.figure(3)
for sol in sols :
    en = 0.5 * sol[:,1]**2 - np.cos( sol[:,0])
    plt.plot( en)
plt.legend( integrator_labels, loc=2)
plt.title( 'energy')


# long term energy

# the 1.0 = np.cos(0) is to account for that kinetic potential energy is
# # maximal at the initial state and 0 at
plt.figure(4)
for sol in sols_long :
    en = 0.5 * sol[:,0]**2 - np.cos( sol[:,1])
    plt.plot( en[::100])
plt.legend( integrator_labels_long, loc=2)
plt.title( 'long term energy')


# animation

#fig5 = plt.figure(5)
#ims = []
#for i in range( 1, nSteps) :
#    ims.append( (plt.plot( sol_symp[:i,0], sol_symp[:i,1]),) )
#im_ani = animation.ArtistAnimation( fig5, ims, interval=200, repeat_delay=3000, blit=True)

plt.show()
