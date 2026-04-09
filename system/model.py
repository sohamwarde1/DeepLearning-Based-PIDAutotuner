import numpy as np
import math

class SystemModel:

    def __init__(self,system,dt):
        self.A = system[0]
        self.B = system[1]
        self.C = system[2]
        self.D = system[3]
        self.dt = dt

        self.n_states = self.A.shape[0]
        self.state = np.zeros(shape=(self.n_states,1))

    def reset(self,x0=None):
        if x0 is None:
            self.state = np.zeros_like(self.state)
        else:
            self.state = x0.copy()

    def step(self, u):
        x_dot = (self.A @ self.state) + (self.B @ u)
        self.state = self.state + (x_dot * self.dt)
        return self.state
    
    def output(self,u):
        y = (self.C @ self.state) + (self.D @ u)
        return y


