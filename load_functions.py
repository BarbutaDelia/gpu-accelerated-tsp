import configparser


def read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    options = {
        "visualize": config.getboolean("DEFAULT", "visualize"),
        "generations": config.getint("DEFAULT", "generations"),
        "mutation_rate": config.getfloat("DEFAULT", "mutation_rate"),
        "population_size": config.getint("DEFAULT", "population_size"),
    }
    return options


def read_cities_with_start(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # The last line specifies the starting city
        starting_city_name = lines[-1].strip()

        city_names = []
        coordinates = []
        for line in lines[:-1]:  # Process all lines except the last
            parts = line.strip().split(" ")
            city_names.append(parts[0])
            x, y = map(float, parts[1:3])
            coordinates.append((x, y))

        return city_names, coordinates, starting_city_name