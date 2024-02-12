#Split a dictionary using map function
marks = {'Science':[88,89,62,95],'Language':[77,78,84,80]}

def list_of_dicts(marks):
    result = map(dict, zip(*[[(key, val) for val in value] for key, value in marks.items()]))
    return list(result)

print("Split said dictionary of lists into list of dictionaries:")
print(list_of_dicts(marks))