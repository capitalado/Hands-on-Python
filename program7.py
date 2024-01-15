#Else block display done after successful execution of a loop
print("Enter any number Greater than zero: ",end='')
x = int(input())
if x == 0:
    print("Oops! seems you've entered a wrong Input.")
else:
    print("Done, Loop executed successfully!")
