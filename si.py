# p= float(input("Enter the Principle ammount: "))
# r= float(input("Enter the rate of interest: "))
# t= float(input("Enter the Time period: "))
# si=((p*r*t)/100)
# print("The simple interest for principle amount "+ str(p) + " is " + str(si))


# A = P(1 + R/100)^T


p= float(input("Enter the Principle ammount: "))
r= float(input("Enter the rate of interest: "))
t= float(input("Enter the Time period: "))
a=p*(pow(1+(r/100),t))
ci=a-p
print("The compound interest for principle amount "+ str(p) + " is " + str(ci))