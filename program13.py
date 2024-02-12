#swap two numbers withoout a 3rd variable
num1 = int(input('Enter the 1st number: '))
num2 = int(input('Enter the 2nd number: '))
print('Before Swapping, num1 = ',num1,'num2 = ',num2)
num1,num2 = num2,num1
print('After Swapping, num1 = ',num1,'num2 = ',num2)