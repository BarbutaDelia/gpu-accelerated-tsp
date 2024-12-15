## Genetic algorithm to solve the Traveling Salesman Problem

The problem states that given a list of of cities and their coordinates, we need to find the shortest route that starts from a city, passes all the cities without repeating any city and then returns to the source city.

### Input data

The program takes as input a list of cities, their coordonates and the source city.
The program takes its input from _input.txt_ file.

Example of input containing 8 cities. On the last line is the name of the city the paths have to start from:
```
A 0.75 0
B 1 1.5
C 2.5 0.5
D 2 2.5
E 1.5 0.5
F 2 1.5
G 2.5 2
H 2.5 2
A
```

### High-level pseudocode of the algorithm


1. **Preprocessing**:
   - Calculate the distance matrix from the city coordinates.


2. **Initialize Population**:
   - Generate initial population of random routes (permutations of cities).
   - Ensure each route starts with the correct city.


3. **Determine Elitism**:
   - Calculate `elite_count` as a percetange of the population size.


4. **Repeat for `generations` iterations**:
    - Evaluate Fitness:
        - For each individual in the population, calculate its fitness:
          - Fitness = 1 / total route distance (minimizing distance maximizes fitness).

    - Select Elites:
        - Identify the top `elite_count` individuals with the highest fitness. They are directly copied into the next generation.

    - Generate Children:
        - While there are remaining slots in the population:
          - Select two parents using roulette wheel selection.
          - Perform crossover to generate two offspring.
          - Mutate each offspring with probability `mutation_rate`.
          - Ensure offspring start with the `starting_city_index`.
          - Add offspring to the new population.

    - Form Next Generation:
        - Combine `elites` and the newly generated offspring to form the new population.


5. **Select the Best Individual**:
   - Evaluate fitness for the final population.
   - Identify the individual with the highest fitness as the best route.
   - Calculate the total distance of the best route.


6. **Return the Best Route and its Distance**.

