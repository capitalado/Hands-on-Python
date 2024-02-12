#Reverse a String
def reverse_string(s):
    return s[::-1]

# Test the function
original_string = input('Enter string: ')
reversed_string = reverse_string(original_string)
print(reversed_string)
