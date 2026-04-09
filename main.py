from controller.PID import PID
from cost.cost import Cost
from simulation.runner import Runner
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

pid = PID(kp=10, ki=0.5, kd=0.3, dt=dt)
history = Runner(system=system,controller=pid,setpoint=setpoint,T=50,dt=dt,u_ini=[0]).run()
cost = Cost(setpoint=1.0,history=history).cost_function()

print(cost)
print(history[-1][0])



# Extract data
y_vals = []
u_vals = []
for h in history:
    y_vals.append(h[0].squeeze())
    u_vals.append(h[1].squeeze())

t = np.arange(len(y_vals))
# Handle setpoint (scalar or array)
if np.isscalar(setpoint):
    sp_vals = [setpoint] * len(t)
else:
    sp_vals = setpoint

# Plot output vs setpoint
plt.figure()
plt.plot(t, y_vals, label="Output (y)")
plt.plot(t, sp_vals, '--', label="Setpoint")
plt.xlabel("Time step")
plt.ylabel("Output")
plt.legend()
plt.title("System Response")

# Plot control input
# plt.figure()
# plt.plot(t, u_vals, label="Control Input (u)")
# plt.xlabel("Time step")
# plt.ylabel("Input")
# plt.legend()
# plt.title("Control Effort")

plt.show()