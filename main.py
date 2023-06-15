"""

This file showcases a Formula 1 simulation model developed as a part of a dissertation titled 
    'Understanding the Complexities of Formula 1 Race Strategy: A Simulation-Based Approach'. 

The code demonstrates how the model can be used to simulate Formula 1 races and visualise the results. 
Specifically, this file parametrises the model to simulate the 2023 Bahrain Grand Prix for the top 7 drivers.



Acknowledgements:

    - This code uses FastF1 library, created by theOehrly, 
        as a source of real-world race data.

    - This code uses Matplotlib library, developed by Michael Droettboom, et al.,
        to visualise the results of the simualted races and real-world data. 

"""

from racePlotter import *

from race import Race
from driver import Driver
from track import Track


"""
    Create and Parametrise drivers to be simulated
"""
ver1 = Driver("VER", 1, 0, 0, pit_in_laps=[14, 36, 40], pit_tyres=["soft", "soft", "hard"], 
               starting_compound="soft", color="#0335fc")

per11 = Driver("PER", 2, 0.2, 0, pit_in_laps=[17, 34, 40], pit_tyres=["soft", "soft", "soft"], 
               starting_compound="soft", color="#5973d9")

lec16 = Driver("LEC", 3, 0, 0.6, pit_in_laps=[13, 33, 15], pit_tyres=["hard", "hard", "soft"], 
               starting_compound="soft", color="#fc2121")

sai55 = Driver("SAI", 4, 0.2, 0.6, pit_in_laps=[13, 31, 40], pit_tyres=["hard", "hard", "hard"], 
               starting_compound="soft", color="#e86868")

alo14 = Driver("ALO", 5, 0, 0.6, pit_in_laps=[14, 34, 40], pit_tyres=["hard", "hard", "hard"], 
               starting_compound="soft", color="#10b569")

rus63 = Driver("RUS", 6, 0.05, 1, pit_in_laps=[12, 30, 40], pit_tyres=["hard", "hard", "hard"], 
               starting_compound="soft", color="#1ceb95")

ham44 = Driver("HAM", 7, 0.1, 1, pit_in_laps=[12, 30, 40], pit_tyres=["hard", "hard", "hard"], 
               starting_compound="soft", color="#0fd9c1")

# Adjust parameters for individual drivers
ver1.tyre.age = 4
alo14.tyre.age = 5
ham44.tyre.age = 4

# Store drivers to be simulated
drivers = [ver1, per11, lec16, sai55, alo14, rus63, ham44]

# Create Track object
bahrain_nternational_circuit = Track(base_laptime="1:35.708")

# Create race object, pass the Track and list of drivers who are to be simulated
bahrainGP = Race(bahrain_nternational_circuit, drivers)

# Simulate the race
bahrainGP.simulate_race()


# Plot simulation results
#plot_simulation_results(drivers)

#plot_positions(bahrainGP)


# Plot real drivers
real_drivers = [("VER", "#0335fc"), ("PER", "#5973d9"), ("LEC", "#fc2121"), 
                ("SAI", "#e86868"), ("ALO", "#10b569"), ("RUS", "#1ceb95"), ("HAM", "#0fd9c1")]

#laptime_overlay_plot(drivers, real_drivers)
