# Formula 1 Strategy Simulation
The simulation is used to evaluate hypothetical race scenarios, allowing the assessment of various strategies and their impact on the race outcome.

Effective strategy plays a vital role in securing victory in Formula 1 races, and as regulations impose greater constraints on teams, the importance of simulation becomes increasingly apparent. This implementation of the strategy simulation tool, builds upon previous research by introducing techniques for parameterising the model and visualizing the results. The implementation also introduces an innovative approach to overtaking that considers probabilities, departing from the conventional notion that superior pace guarantees successful overtakes. By addressing these key elements, this project contributes to enhancing strategic decision-making in the sport.

## Features
Fuel Mass Reduction Model: Simulates fuel consumption throughout the race, affecting the car's weight and performance.

Tyre Wear Model: Simulation currently includes three different dry tyre compounds with individual wear models, accurately reflecting tyre degradation over laps. Users are given ability to parametrise each tyre compound individually and easily create new ones.

 Pit Stop Considerations: Factors affecting pit stops, such as time spent on pit lane drive thru, time spent performing the pit stop as well as unexpected random factors are taken into account.

Starting Performance Model: The simulation models the impact of various factors on a driver's starting performance, such as driver’s starting position.

 Chance-Based Overtaking Model: An innovative overtaking model that considers both pace advantage and chance, determining the likelihood of successful overtaking manoeuvres.

Parameter Obtaining Methods: The simulation comes with a set of functions for used to obtain parameters based on historical race data, allowing for fine tuning of the simulation's accuracy.

Race Time Line Graph: Visualizes race times to identify key events like pit stops, mistakes, and strong performance of drivers.

Driver position evolution chart: Displays each driver's position throughout the race, making overtaking manoeuvres and overall performance easy to analyse.

Validation with Real Race Data: The simulation provides a set of function for easy comparison its results with real race data.


## Built With
 - Python
 - NumPy
 - Matplotlib

## Demo
