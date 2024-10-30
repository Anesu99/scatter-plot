import matplotlib.pyplot as plt

def plot_data(file_path):

    with open(file_path, 'r') as my_file:
        x_coords = []
        y_coords = []

        my_file.readline()

        # Read coordinates from the file
        for line in my_file:
            coords = line.split(',')
            x_coords.append(float(coords[0]))
            y_coords.append(float(coords[1]))

    # Print the coordinates for debugging
    print("X Coordinates:")
    for item in x_coords:
        print(item)

    print("Y Coordinates:")
    for item in y_coords:
        print(item)

    # Create the scatter plot
    plt.scatter(x_coords, y_coords)
    plt.xlabel('X Coordinates')
    plt.ylabel('Y Coordinates')
    plt.title('Scatter Plot of Coordinates')
    plt.grid(True)
    plt.show()

plot_data('C:/Users/MY PC/Downloads/x_y_coordinates.txt')