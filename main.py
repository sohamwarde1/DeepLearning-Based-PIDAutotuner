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
best_params, best_cost = random_search.tune()
random_search.replay_best(random_search.best_records,setpoint)

history = random_search.best_records[-1]


record = random_search.best_records[-1]
history = record["history"]

y_vals = [y for y, _ in history]
u_vals = [u for _, u in history]
t = range(len(y_vals))
plt.ioff()
plt.figure()

plt.plot(t, y_vals, label="Output (y)")
plt.plot(t, [setpoint]*len(t), 'k--', label="Setpoint")

plt.title(
    f"Best Controller: Kp={record['kp']:.2f}, Ki={record['ki']:.2f}, Kd={record['kd']:.2f}"
)

plt.xlabel("Time step")
plt.ylabel("Output")
plt.legend()
plt.grid()

plt.show()