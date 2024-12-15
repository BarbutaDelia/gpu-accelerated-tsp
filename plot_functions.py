import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

def plot_cities(city_names, coordinates):
    x_coords = [coord[0] for coord in coordinates]
    y_coords = [coord[1] for coord in coordinates]

    plt.figure(figsize=(8, 8))

    # Plot the cities
    plt.scatter(x_coords, y_coords, c='blue', s=100, label="Cities")  # City points

    # Add city names
    for i, name in enumerate(city_names):
        plt.text(x_coords[i] + 0.1, y_coords[i] + 0.1, name, fontsize=10, color="red")

    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("City Locations")
    plt.grid(True)
    plt.legend()
    plt.show()


# Plot cities and shortest path
def plot_cities_with_route_and_arrows(city_names, coordinates, route):
    x_coords = [coordinates[city][0] for city in route]
    y_coords = [coordinates[city][1] for city in route]

    # Close the loop by appending the starting city at the end of the route
    x_coords.append(coordinates[route[0]][0])
    y_coords.append(coordinates[route[0]][1])

    plt.figure(figsize=(8, 8))

    plt.scatter(x_coords[:-1], y_coords[:-1], c='blue', s=100, label="Cities")

    # Add city names
    for i, city in enumerate(route):
        plt.text(coordinates[city][0] + 0.1, coordinates[city][1] + 0.1, city_names[city], fontsize=10, color="red")

    # Draw arrows for the path
    for i in range(len(route)):
        start = (coordinates[route[i]][0], coordinates[route[i]][1])
        end = (coordinates[route[(i + 1) % len(route)]][0], coordinates[route[(i + 1) % len(route)]][1])
        arrow = FancyArrowPatch(start, end, arrowstyle='->', color='green', mutation_scale=15, linewidth=1.5)
        plt.gca().add_patch(arrow)

    # Highlight the starting city
    plt.scatter([coordinates[route[0]][0]], [coordinates[route[0]][1]], c='orange', s=200, label="Start/End City")

    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("City Locations with Shortest Path and Directions")
    plt.grid(True)
    plt.legend()
    plt.show()