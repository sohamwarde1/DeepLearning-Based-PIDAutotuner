from simulation.runner import Runner



class Cost:

    def __init__(self,setpoint,history):
        self.setpoint = setpoint
        self.history = history

    def cost_function(self):
        error_sum = 0

        for y, _ in self.history:
            error = self.setpoint - y
            error_sum += error**2

        return error_sum