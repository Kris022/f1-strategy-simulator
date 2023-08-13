# Formula 1 Strategy Simulation
See demo video in the [Demo](#my-section) section below.
## Features

- **Fuel Mass Reduction Model**: Simulates fuel consumption throughout the race, dynamically affecting the car's weight and performance, providing a realistic experience for strategists.

- **Tyre Wear Model**: The simulation includes three different dry tyre compounds, each with its individual wear model, precisely reflecting tire degradation over laps. Users have the flexibility to parameterize each tyre compound individually and effortlessly create new ones.

- **Pit Stop Considerations**: Factors affecting pit stops, such as time spent on pit lane drive-thru, time spent performing the pit stop, and unexpected random factors, are taken into account, adding depth to strategic planning.

- **Starting Performance Model**: The simulation accurately models the impact of various factors on a driver's starting performance, including the driver's starting position, providing insights into initial race dynamics.

- **Chance-Based Overtaking Model**: An innovative overtaking model that considers both the pace advantage and chance, providing a realistic assessment of the likelihood of successful overtaking maneuvers.

- **Parameter Obtaining Methods**: The simulation includes a set of functions for obtaining parameters based on historical race data, allowing for fine-tuning of the simulation's accuracy to match real-world scenarios.

- **Race Time Line Graph**: Visualizes race times, enabling users to identify key events such as pit stops, mistakes, and exceptional driver performances throughout the race.

- **Driver Position Evolution Chart**: Displays each driver's position throughout the race, making overtaking maneuvers and overall performance easy to analyze and comprehend.

- **Validation with Real Race Data**: The simulation provides a set of functions for easy comparison of its results with real race data. FastF1 is a python library and is the main source of real-world data for this project [FastF1 Documentation](https://docs.fastf1.dev/).

   
## Built With

- Python
- NumPy
- Matplotlib

<a name="my-section"></a>
## Demo

### Simulated driver data only
https://github.com/Kris022/f1-strategy-simulator/assets/86967871/6c3d868f-ad90-42a8-9475-98e53c5c3230

### Simulated driver data overlaid with real driver data
https://github.com/Kris022/f1-strategy-simulator/assets/86967871/5a3f79b4-c32d-4fdb-869f-9c4a8609b42d


