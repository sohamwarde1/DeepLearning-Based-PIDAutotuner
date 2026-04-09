class PID:

    def __init__(self,kp,ki,kd,dt):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.dt = dt
        
        self.integral = 0
        self.prev_error = 0

    def compute(self, setpoint, measurement):
        error = setpoint - measurement
        
        self.integral += error * self.dt
        derivative = (error - self.prev_error) / self.dt
        
        self.prev_error = error
        
        return (
            self.kp * error +
            self.ki * self.integral +
            self.kd * derivative
        )
    