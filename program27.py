#Sort a list of dictionaries using lambda. Sort on Colors
models = [{'make': 'Nokia', 'model': 216, 'color':'Black'},
          {'make': 'Mi max', 'model': 2, 'color':'Gold'},
          {'make': 'Samsung', 'model': 7, 'color':'Blue'}]

# Sort the list by 'color' in ascending order
sorted_data = sorted(models, key=lambda x: x['color'])

# Print the sorted list
for item in sorted_data:
    print(item)