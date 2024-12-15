import random
import math


def calculate_distance_matrix(coordinates):
    num_cities = len(coordinates)
    distance_matrix = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance = math.sqrt(
                    (coordinates[i][0] - coordinates[j][0]) ** 2 +
                    (coordinates[i][1] - coordinates[j][1]) ** 2
                )
                distance_matrix[i][j] = round(distance, 2)  # Round to 2 decimals
            else:
                distance_matrix[i][j] = 0.00  # Distance to itself is 0

    return distance_matrix


def initialize_population(num_cities, population_size):
    population = []
    for _ in range(population_size):
        individual = list(range(num_cities))
        random.shuffle(individual)
        population.append(individual)
    return population


def fitness(individual, distance_matrix):
    total_distance = 0
    for i in range(len(individual)):
        from_city = individual[i - 1]
        to_city = individual[i]
        total_distance += distance_matrix[from_city][to_city]
    return 1 / total_distance  # Higher fitness for shorter tours


# ROULETTE WHEEL SELECTION
# Each individual has a probability of being chosen that is proportional to how big his fitness is.
# The function returns the selected individual
def roulette_wheel_selection(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    probabilities = [f / total_fitness for f in fitness_scores]
    return population[random.choices(range(len(population)), probabilities)[0]]


# How this crossover works is that two random indices are chosen. Everything between the 2 indices are copied
# from the parent 1 into child. Now every index from the child which isn't between the chosen indexes is populated
# with remaining genes from the other parent.
def order_crossover(parent1, parent2):
    size = len(parent1)
    child = [-1] * size
    start, end = sorted(random.sample(range(size), 2))
    child[start:end] = parent1[start:end]
    p2_index = 0
    for i in range(size):
        if child[i] == -1:
            while parent2[p2_index] in child:
                p2_index += 1
            child[i] = parent2[p2_index]
    return child


# Mutate by swapping the position of 2 cities
def mutate(individual, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(individual)), 2)
        individual[i], individual[j] = individual[j], individual[i]
    return individual


# Main Genetic Algorithm
def genetic_algorithm(distance_matrix, num_cities, population_size, generations, mutation_rate, starting_city_index):
    # Initialize population
    population = initialize_population(num_cities, population_size)

    # Ensure starting city is fixed
    for individual in population:
        if individual[0] != starting_city_index:
            individual.remove(starting_city_index)
            individual.insert(0, starting_city_index)

    # Elitism: Calculate the number of elite individuals (10% of the population)
    elite_count = population_size // 10

    for _ in range(generations):
        fitness_scores = [fitness(individual, distance_matrix) for individual in population]

        elite_indices = sorted(range(len(fitness_scores)), key=lambda i: fitness_scores[i], reverse=True)[:elite_count]
        elites = [population[i] for i in elite_indices]

        # Generate offspring for the remaining population
        offspring = []
        for _ in range((population_size - elite_count) // 2):
            parent1 = roulette_wheel_selection(population, fitness_scores)
            parent2 = roulette_wheel_selection(population, fitness_scores)
            child1 = order_crossover(parent1, parent2)
            child2 = order_crossover(parent2, parent1)

            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)

            # Ensure starting city is fixed in offspring
            if child1[0] != starting_city_index:
                child1.remove(starting_city_index)
                child1.insert(0, starting_city_index)
            if child2[0] != starting_city_index:
                child2.remove(starting_city_index)
                child2.insert(0, starting_city_index)

            offspring.append(child1)
            offspring.append(child2)

        population = elites + offspring

    # Find the best individual in the final population
    fitness_scores = [fitness(ind, distance_matrix) for ind in population]
    best_individual = population[fitness_scores.index(max(fitness_scores))]
    best_distance = 1 / max(fitness_scores)
    return best_individual, best_distance
