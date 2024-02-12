#Function that accepts different values as params
#and return a list
userString = input('Enter a string: ')
newlist = []
def myFunct(x):
    for i in x:
        newlist.append(i)
    print(newlist)
    
myFunct(userString)