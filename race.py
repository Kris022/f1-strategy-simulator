import random
from helper import *

class Race:
    def __init__(self, track, drivers):

        self.track = track  # Allows access to track parameters
        self.drivers = drivers  # Holds participants of the race

        self.base_laptime_seconds = lap_time_to_seconds(self.track.base_laptime)    # Base lap time converted to seconds represented as a float

        self.laptime_deviation = False # Determines if small inconsistencies in lap time (which aim to simulate driver error) are allowed 

    def get_laptime(self, driver):
        laptime = self.base_laptime_seconds + driver.driver_skill + driver.car_performance \
            + driver.get_fuel_load_panelty() + driver.get_tyre_degradation_panelty()
        
        if self.laptime_deviation: laptime += random.uniform(0, 1.) 

        return laptime
    
    def perform_pitstop(self, driver):
        if driver.is_entering_pit_lane():
            driver.put_on_next_tyre() # Change Tyre
            return self.track.pit_in_panelty # Return pit lane entry drive through panelty
        
        elif driver.is_leaving_pit_lane():
            return self.track.pit_out_panelty + random.uniform(2, 3)
        else:
            return 0
    
    def perform_race_start(self, driver):
        if driver.current_lap == 1:
            driver_row = (driver.start_position - 1) % 20 // 2 + 1 # Get the row the driver is starting on
            laptime = driver_row * self.track.grid_position_panelty # Penalise drivers starting further back
            return laptime
        return 0

    def perform_overtakes(self):
        # Sort drivers in order after the latest lap 
        recent_positions = self.get_drivers_in_order()

        # If driver is not the first in the list
        for d in range(1, len(recent_positions)):
            # Perform overtking calculation for the driver
            current_driver = self.get_driver_by_name(recent_positions[d][0])
            driver_ahead = self.get_driver_by_name(recent_positions[d-1][0])

            gap = current_driver.get_total_time() - driver_ahead.get_total_time()

            if gap < self.track.gap_to_overtake:
                overtake = random.randint(0, 1)
                if overtake > 0:
                    # current driver panelty
                    current_driver_panelty = current_driver.get_last_laptime() + 0.2          
                    # defending driver panelty
                    driver_ahead_panelty = driver_ahead.get_last_laptime() + 0.5
                else:
                     # current driver panelty
                    current_driver_panelty = current_driver.get_last_laptime() + 0.5          
                    # defending driver panelty
                    driver_ahead_panelty = driver_ahead.get_last_laptime() + 0.2
                
                # Penalise drivers after attempted manouver
                current_driver.update_last_laptime(current_driver_panelty)
                driver_ahead.update_last_laptime(driver_ahead_panelty)

    def step(self):
        # For each of the drivers
        for i in range(0, len(self.drivers)):
            driver = self.drivers[i]

            # Calculate laptime
            laptime = self.get_laptime(driver)

            # Apply race start panelty
            laptime += self.perform_race_start(driver)

            # Check for pit stops
            if driver.has_pit_stops_left():
                laptime += self.perform_pitstop(driver)

            # Save laptime
            driver.save_laptime(laptime)

            # Increment driver lap
            driver.start_new_lap()

        # Overtaking
        self.perform_overtakes()
        
    def get_driver_by_name(self, name):
        for driver in self.drivers:
            if name == driver.name:
                return driver
        return None
    
    # Returns a list of [driver name, total race lap time]
    def get_results(self):
        results = []
        for driver in self.drivers:
            results.append([driver.name, driver.get_total_time()])

        return results
    
    # Returns positions for specifed lap
    def get_positions_in_range(self, lap):
        results = []
        for driver in self.drivers:
            results.append([driver.name, driver.get_total_time_in_range(lap)])
        return sorted(results, key=lambda l:l[1])
    
    # Returns finishing order of drivers
    def get_drivers_in_order(self):
        unsorted_results = self.get_results()
        # Sorts items using the second column of the items in multi dim. list
        return sorted(unsorted_results, key=lambda l:l[1])
    
    # Returns a list of drivers with lap times achieved in the finishing order
    def get_results_in_order(self):
        unsorted_results = self.get_results()
        # Sort items using the second column of the items in multi dim. list
        return sorted(unsorted_results, key=lambda l:l[1])

    def simulate_race(self):
        for lap in range(self.track.num_of_laps):
            self.step()
    
    def reset(self):
        pass
    
    # After the race is completed
    # Stores the positons every driver has acheived on each lap
    def save_driver_positions(self):
        for lap in range(1, self.track.num_of_laps+1):
            lap_positions = self.get_positions_in_range(lap)
            for pos in lap_positions:
                driver = self.get_driver_by_name(pos[0])
                driver_position= get_index(driver.name, lap_positions)
                driver.positions.append(driver_position+1)
