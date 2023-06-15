from helper import *
from collections import deque
from tyre import Soft, Medium, Hard

FUEL_LOAD = 80
FUEL_BURN_RATE = 1.2
FUEL_PANELTY = 0.029

class Driver:
    def __init__(self, name, start_position, driver_skill, car_performance, color, starting_compound, pit_in_laps, pit_tyres):
        
        self.name = name    # Driver's name
        self.start_position = start_position
        self.driver_skill = driver_skill # Panelty due to driver ability (in seconds) 

        self.position = start_position # Holds position of the driver throughout the race

        self.car_performance = car_performance # Car perfomrnace panelty (in seconds)
        self.current_lap = 1 # Track the lap the car is on

        # Fuel mass reduction parameters
        self.fuel_load = FUEL_LOAD              # Starting fuel load of the car
        self.fuel_burn_rate = FUEL_BURN_RATE    # Amount of fuel lost each lap (in kg of fuel per lap)
        self.fuel_panelty = FUEL_PANELTY        # Amount of time lost due to fuel load (in seconds per kg of fuel)  
        
        # Tyre degradation parameters
        self.tyre = None
        self.put_on_tyre(starting_compound)

        # Driver pit stops
        self.pit_in_laps = deque(pit_in_laps) 
        self.pit_tyres = deque(pit_tyres)

        # Plot parameters
        self.laptime_dictionary = [] # Stores the lap time driver achieved on each lap

        self.positions = [start_position] # Stores the position driver held on each lap

        self.color = color
    
    def get_fuel_load_panelty(self):
        fuel_mass_time_loss = (self.fuel_load * self.fuel_panelty)
        self.fuel_load -= self.fuel_burn_rate   # Reduce fuel mass
        return fuel_mass_time_loss

    def put_on_tyre(self, compound):
        if compound == "soft":
            self.tyre = Soft() # Change the tyre
        elif compound == "medium":
            self.tyre = Medium() # Change the tyre
        elif compound == "hard":
            self.tyre = Hard() # Change the tyre
    
    def put_on_next_tyre(self):
        next_compound = self.pit_tyres.popleft() # Get the next compound
        self.put_on_tyre(next_compound)

    def get_tyre_degradation_panelty(self):
        return self.tyre.get_degradation()
    
    def has_pit_stops_left(self):
        return len(self.pit_in_laps) != 0
    
    # Returns true if driver is entering the pit lane on the current lap
    def is_entering_pit_lane(self):
        return self.current_lap == self.pit_in_laps[0]
    
    # Returns true if driver is leaving the pit lane on the current lap
    def is_leaving_pit_lane(self):
        if self.current_lap == self.pit_in_laps[0] + 1:
            self.pit_in_laps.popleft()
            return True
        return False
    
    # Returns last achieved lap times
    def get_last_laptime(self):
        return self.laptime_dictionary[-1]
    
    # Used to update driver's latest laptime after overtaking maneuver attempt
    def update_last_laptime(self, laptime):
        self.laptime_dictionary[-1] = laptime

    # Saves driver lap time
    def save_laptime(self, laptime):
        self.laptime_dictionary.append(laptime)
    
    # Updates the lap the driver is on
    def start_new_lap(self):
        self.current_lap += 1
    
    # Returns all lap times achieved by the driver as a list 
    # (in the order that they were acheived) 
    def get_laptimes_seconds(self):
        return [t for t in self.laptime_dictionary]
    
    # Returns race laps
    def get_lap_numbers(self):
        return [i for i in range(1, len(self.laptime_dictionary)+1)]
    
    # Returns sum of all race lap times (in seconds)
    def get_total_time(self):
        return sum(self.laptime_dictionary)
    
    # Returns sum of race lap times up to specified lap (in seconds)
    def get_total_time_in_range(self, lap):
        total_laptime = sum(self.laptime_dictionary[0:lap])
        return total_laptime

