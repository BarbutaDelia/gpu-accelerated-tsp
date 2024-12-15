import time
from pprint import pprint
from genetic_algorithm_functions import genetic_algorithm, calculate_distance_matrix
from load_functions import read_config, read_cities_with_start
from plot_functions import plot_cities_with_route_and_arrows

if __name__ == "__main__":
    config_file = "config.ini"
    file_path = "input_100.txt"

    config_options = read_config(config_file)
    city_names, coordinates, starting_city_name = read_cities_with_start(file_path)

    start_time = time.time()

    distance_matrix = calculate_distance_matrix(coordinates)
    starting_city_index = city_names.index(starting_city_name)

    num_cities = len(city_names)

    population_size = config_options["population_size"]
    generations = config_options["generations"]
    mutation_rate = config_options["mutation_rate"]

    best_route, best_distance = genetic_algorithm(
        distance_matrix, num_cities, population_size, generations, mutation_rate, starting_city_index
    )

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Convert the route indices to city names
    best_route_names = [city_names[i] for i in best_route]

    print("Best Route:", " -> ".join(best_route_names))
    print("Best Distance:", best_distance)

    print(f"Algorithm execution time: {elapsed_time:.4f} seconds")

    if config_options["visualize"]:
        plot_cities_with_route_and_arrows(city_names, coordinates, best_route)
