from controller.PID import PID
from cost.cost import Cost
from simulation.runner import Runner
import numpy as np

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

pid = PID(kp=1.0, ki=0.1, kd=0.01, dt=0.01)
history = Runner(system=system,controller=pid,setpoint=1.0,T=5,dt=0.01).run()
cost = Cost(setpoint=1.0,history=history).cost_function()

print(cost)

