#prime number within a range of 25-50
print("Prime numbers within a range of 25-50")
for num in range(25,51):
    if num > 1:
        for i in range(2,num):
            if (num%i) == 0:
                break
            else:
                print(num)
 

