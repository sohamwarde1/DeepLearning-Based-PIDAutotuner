from system.model import SystemModel
from controller.PID import PID

class Runner:
    
    def __init__(self,system, controller,setpoint, T, dt, u_ini):
        self.system = SystemModel(system=system,dt=dt)
        self.system.reset()
        self.controller = controller
        self.setpoint = setpoint
        self.T = T
        self.dt = dt
        self.u_ini = u_ini

    def run(self):
        self.system.reset()
        
        y = self.system.output(self.u_ini)
        history = []
        for t in range(int(self.T/self.dt)):
            u = self.controller.compute(self.setpoint,y)
            y = self.system.output(u)

            self.system.step(u)

            history.append((y,u))
        
        return history




