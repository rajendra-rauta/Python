import numpy as np
import matplotlib.pyplot as plt

# Define the boundaries of the Indian Ocean
# Latitude range: from -60° (south) to 30° (north)
# Longitude range: from 20° E (west) to 120° E (east)
latitude_range = (-60, 30)
longitude_range = (20, 120)

# Define the size of each grid cell in degrees
cell_size_lat = 1  # 1 degree latitude per grid cell
cell_size_lon = 1  # 1 degree longitude per grid cell

# Create arrays for latitudes and longitudes
latitudes = np.arange(latitude_range[0], latitude_range[1], cell_size_lat)
longitudes = np.arange(longitude_range[0], longitude_range[1], cell_size_lon)

# Create grid cells as (latitude, longitude) pairs (bottom-left corner of each cell)
grid_cells = [(lat, lon) for lat in latitudes for lon in longitudes]

# Display total number of grid cells
print(f"Total number of grid cells: {len(grid_cells)}")

# Optional: Plot the grid on a map for visualization
def plot_grid():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_title('Indian Ocean Grid System')

    # Plot grid lines
    for lat in latitudes:
        ax.plot([longitude_range[0], longitude_range[1]], [lat, lat], color='blue', linewidth=0.5)
    for lon in longitudes:
        ax.plot([lon, lon], [latitude_range[0], latitude_range[1]], color='blue', linewidth=0.5)

    # Set the axis limits and labels
    ax.set_xlim(longitude_range)
    ax.set_ylim(latitude_range)
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    plt.show()

# Call the plot function to visualize the grid
plot_grid()            
  