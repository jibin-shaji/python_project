weight = float(input("What is your weight? "))
unit = input("k(g) or L(bs)? ")
if unit.upper() == "K":
    measure= str(weight * 2.2)
    print("Weight is: "+measure +" Lbs")
elif unit.upper() == "L":
    measure= str(weight * 0.45359)
    print("Weight is: "+measure +" Kgs")
else:
    print("Invalid entry")
