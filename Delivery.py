# Create a dictionary to store warehouse locations
warehouse_locations = {
    "Warehouse A": (12.9715987, 77.5945627),  # Example coordinates
    "Warehouse B": (28.7040592, 77.1024902),
    "Warehouse C": (19.076090, 72.877426),
}

# Function to retrieve warehouse location with case-insensitive check
def get_warehouse_location(warehouse_name):
    # Convert input to lower case and check against lower case dictionary keys
    lowercase_locations = {k.lower(): v for k, v in warehouse_locations.items()}
    # Print the lowercase dictionary for debugging
    print(lowercase_locations)
    # Print the lowercase version of the warehouse name for debugging
    print(warehouse_name.lower())
    return lowercase_locations.get(warehouse_name.lower(), "Warehouse not found")

# Test the function
print(get_warehouse_location("Warehouse A"))  # Output: (12.9715987, 77.5945627)
print(get_warehouse_location("Warehouse B"))  # Output: (28.7040592, 77.1024902)
print(get_warehouse_location("Warehouse C"))  # Output: (19.076090, 72.877426)
print(get_warehouse_location("Warehouse X"))  # Output: Warehouse not found