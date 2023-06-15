import matplotlib.pyplot as plt
import fastf1 as ff1
import os
import math
import numpy as np

"""
    
    This code contains funcitons which visualise the simualtion results and real data.
    Note if working with functions desinged to visulaise real race data, set the 
    real_data_enabled variable to True.

    If you do NOT require real data, you can set the variable to False in order
    to omit loading the FastF1 library which slows down execution of the program. 

    Also if using the real data you can change the real_session varaibles to change the real world session for 
    which data is fetched, deafult is set to Bahrain 2023 as this is the session which the demo file 
    is parametrised to simulate.

"""

real_data_enabled = True

real_session = "Bahrain"
real_session_date = 2023
real_session_format = "R" 

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder created at {folder_path}")
    else:
        print(f"Folder already exists at {folder_path}")


if real_data_enabled:
    create_folder_if_not_exists("f1cache")

    ff1.Cache.enable_cache('f1cache') 

    r_session = ff1.get_session(real_session_date, real_session, real_session_format)
    r_session.load()

# Fetches data for driver to be plotted, and plots it on passed axis
def fetch_and_plot_real_driver(name, color, ax):
    laps = r_session.laps.pick_driver(name)
    lap_times = laps[["LapNumber", "LapTime"]]
    # Convert the timedelta data to a numerical value (seconds)
    lap_times['Seconds'] = [td.total_seconds() for td in lap_times['LapTime']]
    ax.plot(lap_times["LapNumber"], lap_times['Seconds'], color=color, label="Real "+name)

# Creates a line chart of real drivers' lap times
def plot_real_race_results(real_drivers):
    fig, ax = plt.subplots()

    for driver in real_drivers:
        fetch_and_plot_real_driver(driver[0], driver[1], ax)

    ax.legend()
    ax.set_xlabel("Lap Number")
    ax.set_ylabel("Lap Time (seconds)")

    plt.show()

# Creates a line chart of simulated drivers' lap times
def plot_simulation_results(simulated_drivers):
    fig, ax = plt.subplots()

    for driver in simulated_drivers:
        ax.plot(driver.get_lap_numbers(), driver.get_laptimes_seconds(), color=driver.color, label="Sim "+driver.name)

    ax.legend()
    ax.set_xlabel("Lap Number")
    ax.set_ylabel("Lap Time (seconds)")

    plt.show()

# Creates a line chart which superimposes simulated and real lap times 
def laptime_overlay_plot(simulated_drivers, real_drivers):
    fig, ax = plt.subplots()

    for driver in simulated_drivers:
        ax.plot(driver.get_lap_numbers(), driver.get_laptimes_seconds(), color=driver.color, label="Sim "+driver.name)

    for driver in real_drivers:
        fetch_and_plot_real_driver(driver[0], driver[1], ax)
        
    ax.legend()
    ax.set_xlabel("Lap Number")
    ax.set_ylabel("Lap Time (seconds)")

    plt.show()

"""
    Position Plotting
"""
def plot_positions(race):
    race.save_driver_positions()

    laps = [i for i in range(0, race.track.num_of_laps+1)]

    # Create a figure and two subplots, sharing the x-axis
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    # Set the x-axis limits and labels
    ax1.set_xlim([0, race.track.num_of_laps])
    ax1.set_xlabel("Lap Number")
    
    for driver in race.drivers:
        # Plot the positions as a line graph
        ax2.plot(laps, driver.positions,
                 color=driver.color, label=driver.name)

    # Set the left y-axis limits and label
    ax1.set_ylim([-0.5, len(race.drivers)-0.5])
    ax1.set_yticks(range(len(race.drivers)))
    axlabels = [x.name for x in race.drivers]
    ax1.set_yticklabels(axlabels)
    ax1.set_ylabel("Driver Name")

    # Set the right y-axis limits, ticks, and label
    ax2.set_ylim([0.5, len(race.drivers)+0.5])
    ax2.set_yticks([driver.start_position for driver in race.drivers])
    ax2.set_ylabel("Position")

    plt.title("Simulated Race Positions")

    # Display the plot
    plt.show()


def fit_line_to_race(driver):
    laps = r_session.laps.pick_driver(driver)
    lap_times = laps[["LapNumber", "LapTime"]]
    # Convert the timedelta data to a numerical value (seconds)
    lap_times['Seconds'] = [td.total_seconds() for td in lap_times['LapTime']]

    # Exclude first from lap_times as it is NaN
    lap_times = lap_times[1:]
    lap_times = lap_times[lap_times['Seconds'] <= 100.0]

    # fit a line to the data using polyfit
    coefficients = np.polyfit(lap_times['LapNumber'], lap_times['Seconds'], 1)
    m = coefficients[0]
    b = coefficients[1]
    print("m = ", m, "b = ", b)

    plt.scatter(lap_times['LapNumber'], lap_times['Seconds'], label=driver)
    plt.plot(lap_times['LapNumber'], m*lap_times['LapNumber'] + b, color='red')

    plt.xlabel('Lap Number')
    plt.ylabel('Lap Time (Seconds)')
    plt.title('Lap time improvement due to fuel mass reduction')
    plt.legend()
    plt.show()

def scatter_stint_laptimes(drivers, stint):
    for driver in drivers:
        laps = r_session.laps.pick_driver(driver)
        filtered_times = laps[laps["Stint"] == stint]
        lap_times = filtered_times[["LapNumber", "LapTime"]]
        # Convert the timedelta data to a numerical value (seconds)
        lap_times['Seconds'] = [td.total_seconds() for td in lap_times['LapTime']]
        plt.scatter(lap_times['LapNumber'], lap_times['Seconds'], label=driver)

    plt.xlabel('Lap Number')
    plt.ylabel('Lap Time (Seconds)')
    plt.title('Real Lap Times for Drivers')
    plt.legend()
    plt.show()

def fit_line_to_stint(driver, stint):
    laps = r_session.laps.pick_driver(driver)
    filtered_times = laps[laps["Stint"] == stint]
    lap_times = filtered_times[["LapNumber", "LapTime"]]
    # Convert the timedelta data to a numerical value (seconds)
    lap_times['Seconds'] = [td.total_seconds() for td in lap_times['LapTime']]

    # exclude first and last values from lap_times
    lap_times = lap_times[1:-1]

    plt.scatter(lap_times['LapNumber'], lap_times['Seconds'], label=driver)

    # fit a line to the data using polyfit
    coefficients = np.polyfit(lap_times['LapNumber'], lap_times['Seconds'], 1)
    m = coefficients[0]
    b = coefficients[1]
    print("m = ", m, "b = ", b)

    plt.plot(lap_times['LapNumber'], m*lap_times['LapNumber'] + b, color='red')

    plt.xlabel('Lap Number')
    plt.ylabel('Lap Time (Seconds)')
    plt.title('Real Lap Times for: {0} Stint {1}'.format(driver, str(stint)))
    plt.legend()

    # adjust axis limits to show the line
    x_min, x_max = plt.xlim()
    y_min, y_max = plt.ylim()
    x_range = x_max - x_min
    y_range = y_max - y_min
    plt.xlim(x_min - 0.1*x_range, x_max + 0.1*x_range)
    plt.ylim(y_min - 0.1*y_range, y_max + 0.1*y_range)

    plt.show()
   
def fit_curve_to_stint(driver, stint):
    laps = r_session.laps.pick_driver(driver)
    filtered_times = laps[laps["Stint"] == stint]
    lap_times = filtered_times[["LapNumber", "LapTime"]]
    # Convert the timedelta data to a numerical value (seconds)
    lap_times['Seconds'] = [td.total_seconds() for td in lap_times['LapTime']]

    # Exclude first and last values from lap_times
    lap_times = lap_times[1:-1]
    
    # Check for missing or invalid data
    if np.isnan(lap_times['LapNumber']).any() or np.isnan(lap_times['Seconds']).any():
        print("Error: input array contains missing or invalid data.")
        return

    # Fit a curve to the data using polyfit
    coefficients = np.polyfit(lap_times['LapNumber'], lap_times['Seconds'], 2)
    a = coefficients[0]
    b = coefficients[1]
    c = coefficients[2]
    print("a = ", a, "b = ", b, "c = ", c)

    plt.scatter(lap_times['LapNumber'], lap_times['Seconds'], label=driver)
    x_values = np.linspace(lap_times['LapNumber'].min(), lap_times['LapNumber'].max(), 100)
    y_values = a * x_values ** 2 + b * x_values + c
    plt.plot(x_values, y_values, color='red')

    plt.xlabel('Lap Number')
    plt.ylabel('Lap Time (Seconds)')
    plt.title('Real Lap Times for Driver: {}'.format(driver))
    plt.legend()

    # Adjust axis limits to show the curve
    x_min, x_max = plt.xlim()
    y_min, y_max = plt.ylim()
    x_range = x_max - x_min
    y_range = y_max - y_min
    plt.xlim(x_min - 0.1*x_range, x_max + 0.1*x_range)
    plt.ylim(y_min - 0.1*y_range, y_max + 0.1*y_range)

    plt.show()
