#Elements at even index number
print('Enter your String: ',end='')
str1 = input() 
for i in str1:
    if (str1.index(i))%2 != 0:
        print(i) 
