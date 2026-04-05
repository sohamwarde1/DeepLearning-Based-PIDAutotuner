import numpy as np
import math

class SystemModel:

    def __init__(self,A,B,C,D,dt=0.01):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.dt = dt

        self.n_states = A.shape[0]
        self.state = np.zeros(shape=(self.n_states,1))

    def reset(self,x0=None):
        if x0 is None:
            self.state = np.zeros_like(self.state)
        else:
            self.state = x0.copy()

    def step(self, u):
        self.u = u

        x_dot = (self.A @ self.state) + (self.B @ self.u)
        y = (self.C @ self.state) + (self.D @ u)

        self.state = self.state + (x_dot*self.dt)

        return y

A = np.array([[-1]])
B = np.array([[1]])
C = np.array([[1]])
D = np.array([[0]])

sys = SystemModel(A, B, C, D)

for _ in range(1000):
    y = sys.step(np.array([[1]]))
    print(y)

