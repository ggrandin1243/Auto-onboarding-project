import matplotlib.pyplot as plt
from pid_template import make_car
from pid_template import update
from pid_template import calculate_desired_acceleration
from pid_template import acceleration_to_throttle_percentage
import numpy as np
K_P = 0.7
K_I = 0.03
K_D = 0.01

STEPS = 550
 
car = make_car(desired_v=20.0, dt=0.1)


times = []
velocities = []
errors = []


for step in range(STEPS):
    acceleration_final, error,car["net_integral"],car["error_prev"] = calculate_desired_acceleration(car, K_P, K_I, K_D)
    throttle_percentage = acceleration_to_throttle_percentage(acceleration_final)

    #adds the current time, velocity, and error to the lists for plotting
    times.append(car["t"])
    velocities.append(car["v"])
    errors.append(error)

    update(car, throttle_percentage)

#plots everything
plt.plot(times, velocities, label="Velocity")
plt.plot(times, errors, label="Error")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.legend()
plt.show()