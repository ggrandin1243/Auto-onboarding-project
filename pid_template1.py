
from dbm import error

import matplotlib.pyplot as plt
import numpy as np


def make_car(desired_v:float=20.0, dt:float=0.1) -> dict:
    """ 
    Generates a dictionary that holds all the car's values. Keeps track of state varaibles.
    """
    car_state_dictionary : dict[str, float] = {
        "v" : 0, #velocity of your car 
        "a" : 0, #acceleration of your car
        "t" : 0, #time of your car
        "x" : 0, #position of your car
        "dt" : dt, #time step of your car, how much the time changes every time you update/step
        "desired_v" : desired_v, #desired velocity of your car, the velocity you want to maintain
        "step" : 0,
    
        "error_prev" : None,
        "net_integral" : 0.0
    }
    return car_state_dictionary

def update(car: dict, throttle_perc: float, mass: float = 1000, max_throttle_force: float = 5000, friction: float = 2.0) -> None:
        
        force = throttle_perc * max_throttle_force
        car["a"] = (force / mass) - friction
        car["v"] += car["a"] * car["dt"]
        car["x"] += car["v"] * car["dt"]
        car["t"] += car["dt"]
        car["step"] += 1


def calculate_desired_acceleration(car: dict, K_P: float, K_I: float = 0.0, K_D: float = 0.0) -> tuple[float, float]:

        
        error = car["desired_v"] - car["v"]
        car["error_prev"] = (error / car["dt"])
        car["net_integral"] += (error * car["dt"])

        #adds K_P, K_I, and K_D to the calculate_desired_acceleration function.
        acceleration_desired = (K_P * error) 
        acceleration_desired += (K_I * car["net_integral"])
        acceleration_desired += (K_D * car["error_prev"])

        #updates the car's net_integral and error_prev values in the car dictionary
        return (acceleration_desired, error,car["net_integral"],car["error_prev"])


def acceleration_to_throttle_percentage(acceleration_desired: float, mass: float = 1000, max_throttle_force: float = 5000) -> float:
       
        max_acceleration = (max_throttle_force /mass)

        throttle_percentage = (acceleration_desired / max_acceleration)
        throttle_percentage = np.clip(throttle_percentage, -1, 1)
        return throttle_percentage
        #gets throttle % and then limits it to -1, 1.



