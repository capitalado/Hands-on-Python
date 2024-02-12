chars = {'a','b','E','f','a','i','o','U','a'}
#Removing the duplicates
dupli = list(set(chars))

#Convert to uppercase
print('The Uppercase: ',list(map(lambda x: x.upper(), dupli)))
print('The Lowercase: ',list(map(lambda x: x.lower(), dupli)))

