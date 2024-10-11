import numpy as np

# Define grid parameters
grid_size = 10  # Number of cells along one dimension
cell_size = 1.0  # Size of each cell in kilometers

# Initialize grid
grid = np.zeros((grid_size, grid_size))  # Grid with default cost of 0

# Example function to set costs based on environmental factors
def set_cell_cost(grid, x, y, wind, waves, currents):
    base_cost = 1.0  # Base cost of moving through a cell
    wind_cost = wind[y, x]
    wave_cost = waves[y, x]
    current_cost = currents[y, x]
    total_cost = base_cost + wind_cost + wave_cost + current_cost
    grid[y, x] = total_cost

# Initialize environmental factors
wind = np.random.rand(grid_size, grid_size)  # Random wind costs 
waves = np.random.rand(grid_size, grid_size)  # Random wave costs
currents = np.random.rand(grid_size, grid_size)  # Random current costs

# Set costs in the grid
for y in range(grid_size):
    for x in range(grid_size):
        set_cell_cost(grid, x, y, wind, waves, currents)

# Convert real-world coordinates to grid coordinates
def world_to_grid(x, y, cell_size):
    return int(x / cell_size), int(y / cell_size)

# Example usage
real_world_x = 15.5
real_world_y = 20.7
grid_x, grid_y = world_to_grid(real_world_x, real_world_y, cell_size)
print(f"Real-world coordinates ({real_world_x}, {real_world_y}) map to grid coordinates ({grid_x}, {grid_y})")
