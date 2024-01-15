#List Elements at odd index positions
mylist = ['Red','Blue','Green']
print('Elements at odd index positions are: ')
for i in mylist:
    if (mylist.index(i)) % 2 != 1:
        print(i)