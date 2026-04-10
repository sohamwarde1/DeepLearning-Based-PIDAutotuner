class Cost:

    def __init__(self, setpoint, history):
        self.setpoint = setpoint
        self.history = history
        self.cost_list = []

    def cost_function(self):
        w_e = 1.0
        w_u = 0.01
        w_d = 0.1
        w_o = 2.0

        cost = 0
        prev_u = self.history[0][1]

        for y, u in self.history:
            val = 0

            e = self.setpoint - y

            # tracking
            val += w_e * (e**2)

            # control effort
            val += w_u * (u**2)

            # smoothness
            du = u - prev_u
            val += w_d * (du**2)

            # overshoot
            overshoot = max(0, -e)
            val += w_o * (overshoot**2)

            cost += val
            self.cost_list.append(val)

            prev_u = u

        return cost