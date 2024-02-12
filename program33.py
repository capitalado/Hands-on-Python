#List with maximum and minimum using lambda
list1 = [[0],[1,3],[5,7],[9,11],[13,15,17]]

# Using lambda to find the maximum value in each sublist
max_values = list(map(lambda x: max(x), list1))
print("Maximum values:", max_values)

# Using lambda to find the minimum value in each sublist
min_values = list(map(lambda x: min(x), list1))
print("Minimum values:", min_values)