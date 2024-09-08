import matplotlib.pyplot as plt
import cartopy.crs as ccrs

def create_grid(extent, grid_spacing):
    """
    Creates a grid on a map.

    Args:
        extent: The extent of the map as a tuple (min_lon, max_lon, min_lat, max_lat).
        grid_spacing: The spacing between grid lines in degrees.
    """

    # Set up the map projection
    proj = ccrs.PlateCarree()

    # Create the figure and axes
    fig, ax = plt.subplots(subplot_kw={'projection': proj})

    # Draw the coastlines
    ax.coastlines()

    # Create the grid
    lon_min, lon_max, lat_min, lat_max = extent
    lon_ticks = np.arange(lon_min, lon_max + grid_spacing, grid_spacing)
    lat_ticks = np.arange(lat_min, lat_max + grid_spacing, grid_spacing)

    ax.set_xticks(lon_ticks)
    ax.set_yticks(lat_ticks)
    ax.grid(True, linestyle='--')

    # Set the map extent
    ax.set_extent(extent)

    # Show the plot
    plt.show()

# Example usage
extent = (30, 100, -30, 30)  # Extent of the Indian Ocean
grid_spacing = 10  # Grid spacing in degrees

create_grid(extent, grid_spacing)