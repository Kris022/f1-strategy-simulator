

class Track:
    def __init__(self, base_laptime, gap_to_overtake=3., pit_in_panelty=5, pit_out_panelty=18.5, num_of_laps=57, grid_position_panelty=0.2):
        self.base_laptime = base_laptime
        self.pit_in_panelty = pit_in_panelty    # Time panelty for pit entry (seconds)
        self.pit_out_panelty = pit_out_panelty  # Time panelty for leaving the pitlane (seconds)
        self.grid_position_panelty = grid_position_panelty  # Time penalty for starting on a grid row farther from the start line (seconds)
        self.num_of_laps = num_of_laps  # Number of laps in the race
        self.gap_to_overtake = gap_to_overtake
        
