"""

 Scorched Nebraska World Server File
 Janusz Jeremiasz Filipiak
 (c) 2024
 Map Loader front end for (map) => (lattice) interface.

 Uses Google Maps & Elevation API

 Developed in Utah, Colorado, Nevada, California USA

 IMPORTANT:
 Early version, run: mkdir dbits.

 NOTES:
 Regularly maintain dbits/
 Flask API Coming soon

"""

import requests
from mapsloader import WorldLattice, AlgorithmicMemory
from math import cos, sin, radians

def geocode_address(address, api_key):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get('results')
        if results:
            location = results[0]['geometry']['location']
            return location['lat'], location['lng']
    raise ValueError("Failed to geocode address")

# Google API functions
GOOGLE_API_KEY = 'AIzaSyAb59YZVZEVdzZeJDV8b05Bur5rl9xsY7Y'

def get_altitude_for_multiple_locations(locations, api_key):
    """
    Fetch altitudes for multiple latitude and longitude pairs using Google Elevation API.
    :param locations: List of (lat, lon) tuples.
    :param api_key: Google API key.
    :return: List of altitudes corresponding to each (lat, lon) pair.
    """
    # Construct the locations string for the API request
    location_str = "|".join([f"{lat},{lon}" for lat, lon in locations])
    url = f"https://maps.googleapis.com/maps/api/elevation/json?locations={location_str}&key={api_key}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code} from the Elevation API.")
        print("Response content:", response.content)
        raise ValueError("Failed to get altitude")
    
    data = response.json()
    status = data.get('status', '')
    
    if status != 'OK':
        print(f"Error: Elevation API returned status '{status}'.")
        print("Response content:", response.content)
        raise ValueError("Failed to get altitude")
    
    results = data.get('results', [])
    altitudes = [result['elevation'] for result in results]
    return altitudes

precision_factor = 1000

# Main script to populate lattice and visualize
def initializeLattice(city = None, region = None):
    # Convert address to GPS coordinates using Google Geocoding API
    if city is None:
        start_address = "3508 Red Rock Dr, Moab UT 84532"
    else:
        start_address = city + ", " + region
    # start_address = "Herald Square, New York, NY"
    # start_address = "ul. Jacka Szarskiego 20a, 30-698 Krakow, Poland"
    start_lat, start_lon = geocode_address(start_address, GOOGLE_API_KEY)

    # Define the grid dimensions
    grid_size = 20  # 40x40 points
    spacing = 100 / 3.28084  # 100 feet to meters

    # Initialize lattice
    try:
        lattice = WorldLattice.WorldLattice.deserialize('lat_test0.dat')
    except FileNotFoundError as e:
        lattice = WorldLattice.WorldLattice('lat_test0.dat')

    # Create a list of (lat, lon) tuples for the grid points
    locations = []
    for i in range(-grid_size // 2, grid_size // 2 + 1):
        for j in range(-grid_size // 2, grid_size // 2 + 1):
            if abs(i) + abs(j) <= grid_size // 2:
                # Convert offsets to GPS coordinates
                dx = i * spacing * cos(radians(45)) - j * spacing * sin(radians(45))
                dy = i * spacing * sin(radians(45)) + j * spacing * cos(radians(45))
                lat = start_lat + dx / 111320
                lon = start_lon + dy / (111320 * cos(radians(start_lat)))
                locations.append((lat, lon))

    # Fetch altitudes for all locations in a single API call
    altitudes = get_altitude_for_multiple_locations(locations, GOOGLE_API_KEY)

    # print(altitudes)

    x_lat = int(locations[0][0] * precision_factor)
    y_lon = int(locations[0][1] * precision_factor)
    z_alt = int(altitudes[0])

    # print(x_lat, y_lon, z_alt)

    # Insert dbits into the lattice with the fetched altitude data
    for (lat, lon), alt in zip(locations, altitudes):
        int_lat = int(lat * precision_factor) - x_lat
        int_lon = int(lon * precision_factor) - y_lon
        int_alt = int(alt) - z_alt
        dbit = lattice.am.retrieve(int_lat, int_lon, int_alt)
        if dbit is None:
            lattice.insert({
                'type' : 'map_vertex',
                'lat' :lat,
                'lon' :lon,
                'alt' :alt
                }, int_lat, int_lon, int_alt)

    # Visualize the lattice
    lattice.serialize()
    # lattice.visualize_lattice()
    # # in_development lattice.serialize()

    latticecopy = WorldLattice.WorldLattice.deserialize('lat_test0.dat')

    latticecopy.visualize_lattice()

    return latticecopy

    # In memory browser:
    # AlgorithmicMemory.inspectDBit( latticecopy.am.last_rv, latticecopy.am )
    

