import random
import numpy as np
import matplotlib.pyplot as plt
import math
from controller.PID import PID
from cost.cost import Cost
from simulation.runner import Runner


plt.ion()  # interactive mode
fig, ax = plt.subplots()

class RandomSearchPIDTuner:
    def __init__(self,system,setpoint,T,dt,u_ini, n_samples=100):
        """
        simulate_fn: function(Kp, Ki, Kd) -> cost
        n_samples: number of random trials
        """
        self.n_samples = n_samples

        self.system = system
        self.setpoint = setpoint
        self.T = T
        self.dt = dt
        self.u_ini = u_ini
        self.best_cost = float('inf')
        self.best_params = None

        self.log = []

    def simulate(self,kp,ki,kd):
        pid = PID(kp=kp, ki=ki, kd=kd, dt=self.dt)
        history = Runner(system=self.system,
                         controller=pid,
                         setpoint=self.setpoint,
                         T=self.T,dt=self.dt,
                         u_ini=self.u_ini).run()
        cost = Cost(setpoint=self.setpoint,history=history)
        cost_val = np.array(cost.cost_function())
        return cost_val.squeeze(),history

    # ---------- Sampling ----------
    def sample_log(self, low, high):
        return 10 ** random.uniform(math.log10(low), math.log10(high))

    def sample_params(self):
        kp = self.sample_log(0.01, 100)
        ki = self.sample_log(0.001, 10)
        kd = self.sample_log(0.001, 10)
        return kp, ki, kd

    # ---------- Main optimization ----------
    def tune(self):
        for i in range(self.n_samples):
            kp, ki, kd = self.sample_params()

            cost,history = self.simulate(kp, ki, kd)

            self.log.append((kp, ki, kd, cost))

            if cost < self.best_cost:
                self.best_cost = cost
                self.best_params = (kp, ki, kd)

                print(f"[{i}] New best:")
                print(f"    Kp={kp:.4f}, Ki={ki:.4f}, Kd={kd:.4f}")
                print(f"    Cost={cost:.4f}")

                self.update_plot(
                    history,
                    title=f"Kp={kp:.2f}, Ki={ki:.2f}, Kd={kd:.2f}"
                )

        return self.best_params, self.best_cost

    # ---------- Utilities ----------
    def get_log(self):
        return self.log

    def get_best(self):
        return self.best_params, self.best_cost
    
    def update_plot(self,history, title=""):
        setpoint = self.setpoint
        y_vals = [y for y, _ in history]
        t = range(len(y_vals))

        ax.clear()
        ax.plot(t, y_vals, label="Output")
        ax.plot(t, [setpoint]*len(t), '--', label="Setpoint")

        ax.set_title(title)
        ax.legend()
        plt.pause(0.01)