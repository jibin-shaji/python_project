num=int(input("Enter the number to be checked: "))
real= num
l= len(str(num))
# print(l)
i=0
sum=0
while i<l:
    d=num%10
    sum=sum+(pow(d,l))
    num=num//10
    # print(num)
    i+=1
    # print(sum)
if sum == real:
    print("Hurray!!! "+str(real)+" is an Amstrong number ")
else:
    print("OOPS "+str(real)+" is not an Amstrong number ")

