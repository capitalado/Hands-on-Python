#List of tuples, containing city name and population
#Use filter function to extract cities with poop > 2 Million
# Define a list of city-population tuples
cities = [
    ("Gujarat", 8500000),
    ("Mumbai", 4000000),
    ("Maharashtra", 2700000),
    ("Udaipur", 2300000),
    ("Rajkot", 1600000),
    ("North India", 1500000),
    ("Ahmedabad", 1500000),
]

# Define a function to check if a city has a population greater than 2 million
def has_population_greater_than_two_million(city_population):
    return city_population[1] > 2000000

# Use the filter function to extract cities with a population greater than two million
million_plus_cities = list(filter(has_population_greater_than_two_million, cities))

# Print the extracted cities
print(million_plus_cities)