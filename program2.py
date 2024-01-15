#Take Input as comma-separated value
values = input("Enter the comma-sep numbers: ")
list = values.split(",")
tuple = tuple(list)
print("List is: ",list)
print("Tuple is: ",tuple)