weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Filter the list using Lambda
six_letter_days = list(filter(lambda day: len(day) == 6, weekdays))

print(six_letter_days)