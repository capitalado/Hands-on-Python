#Occurence of even and odd, range 10-55
even_count,odd_count = 0,0
x = range(10,55+1)
for i in x:
    #Check for even occurence
    if i % 2 == 0:
        even_count+=1
    #check for odd occurence
    elif i % 2 == 1:
        odd_count+=1
print(even_count," ",odd_count)     