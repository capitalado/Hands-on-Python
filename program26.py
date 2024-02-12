#lambda function that adds 15 to a given number
#Also, the one that multiply argument x and y
x = int(input('Enter the value of x: '))
y = int(input('Enter the value of y: '))
add = lambda x: x + 15
multiply = lambda x,y :x * y
result = add(x)
resulty = multiply(x,y)
print(result,' ',resulty)
