# Formula 1 Strategy Simulation

This Formula 1 Strategy Simulation was designed to evaluate hypothetical race scenarios, providing a detailed assessment of various strategies and their potential impact on the race outcome.

## Motivation

Effective strategy is a crucial factor in securing victory in Formula 1 races, and with increasing regulations imposing constraints on teams, the importance of simulations becomes even more apparent. This implementation of the strategy simulation tool builds upon previous research by introducing advanced techniques for parameterization of the model and visualization of the results. Additionally, it presents an innovative approach to overtaking, incorporating probabilities rather than solely relying on superior pace, thus contributing to enhancing strategic decision-making in the sport.

## Features

1. **Fuel Mass Reduction Model**: Simulates fuel consumption throughout the race, dynamically affecting the car's weight and performance, providing a realistic experience for strategists.

2. **Tyre Wear Model**: The simulation includes three different dry tyre compounds, each with its individual wear model, precisely reflecting tire degradation over laps. Users have the flexibility to parameterize each tyre compound individually and effortlessly create new ones.

3. **Pit Stop Considerations**: Factors affecting pit stops, such as time spent on pit lane drive-thru, time spent performing the pit stop, and unexpected random factors, are taken into account, adding depth to strategic planning.

4. **Starting Performance Model**: The simulation accurately models the impact of various factors on a driver's starting performance, including the driver's starting position, providing insights into initial race dynamics.

5. **Chance-Based Overtaking Model**: An innovative overtaking model that considers both the pace advantage and chance, providing a realistic assessment of the likelihood of successful overtaking maneuvers.

6. **Parameter Obtaining Methods**: The simulation includes a set of functions for obtaining parameters based on historical race data, allowing for fine-tuning of the simulation's accuracy to match real-world scenarios.

7. **Race Time Line Graph**: Visualizes race times, enabling users to identify key events such as pit stops, mistakes, and exceptional driver performances throughout the race.

8. **Driver Position Evolution Chart**: Displays each driver's position throughout the race, making overtaking maneuvers and overall performance easy to analyze and comprehend.

9. **Validation with Real Race Data**: The simulation provides a set of functions for easy comparison of its results with real race data, enhancing its credibility and reliability. We credit FastF1 as the source of real-world data. For more information, refer to [FastF1 Documentation](https://docs.fastf1.dev/).

## Built With

- Python
- NumPy
- Matplotlib

## Demo

### Simulated driver data only
https://github.com/Kris022/f1-strategy-simulator/assets/86967871/6c3d868f-ad90-42a8-9475-98e53c5c3230

### Simulated driver data overlaid with real driver data
https://github.com/Kris022/f1-strategy-simulator/assets/86967871/5a3f79b4-c32d-4fdb-869f-9c4a8609b42d


