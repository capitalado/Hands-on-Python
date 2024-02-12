#Function to find the maximum of three numbers
def myFunc(a,b,c):
    if a==b and b==c:
        print('Repeated Value!')
    elif a > b and a > c:
        print(a,' is Greater than the rest')
    elif b > a and b > c:
        print(b,' is Greater than the rest')
    else:
        print(c,' is the Greatest of all')
        
x = int(input('Enter the first number:'))
y = int(input('Enter the second number:'))
z= int(input('Enter the third number:'))

myFunc(x,y,z)
