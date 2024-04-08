number = float(input("Enter the number to find factorial: "))
i=1
j=number
while i<number:
    j=(j*(number-i))
    print(j, i)
    i+=1
print("Factorial of "+str(number) + " is "+str(j))



