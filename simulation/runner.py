from system.model import SystemModel
from controller.PID import PID

class Runner:
    
    def __init__(self,system, controller,setpoint, T, dt):
        self.system = SystemModel(system=system,dt=dt)
        self.controller = controller
        self.setpoint = setpoint
        self.T = T
        self.dt = dt

    def run(self):
        self.system.reset()

        history = []

        for t in range(int(self.T/self.dt)):
            u = self.controller.compute()
            y = self.system.output(u)

            self.system.step(u)

            history.append((y,u))
        
        return history




