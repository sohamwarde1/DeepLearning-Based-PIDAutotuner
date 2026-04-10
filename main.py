from optimization.optimizer import RandomSearchPIDTuner

import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [0, 1],
    [-2, -0.5]
])

B = np.array([
    [0],
    [1]
])

C = np.array([
    [1, 0]   # output = position
])

D = np.array([
    [0]
])

system = [A,B,C,D]
dt = 0.01
setpoint = 1.0
T = 50
u_ini = [0]
random_search = RandomSearchPIDTuner(system=system,
                                     setpoint=setpoint,
                                     T=T,dt=dt,
                                     u_ini=u_ini,
                                     )
random_search.tune()