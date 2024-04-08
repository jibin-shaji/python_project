# print("Hello world")
import datetime
from datetime import date


name = input("Name of the patient: ")
birth_yr = input("What is the birth year of " + name + "? ")
print(10*'*')
current_day = date.today()
print('Today is '+ str(current_day))
year = datetime.datetime.now().year
this_day = datetime.datetime.now().day
print('Current date is '+str(this_day))
this_month = datetime.datetime.now().month
print('Current Month is '+str(this_month))

print('The year is '+ str(year))
age = year - float(birth_yr)
# is_new = True
print(10*'*' +"Patient Card"+ 10*'*')
print("Patient name is: " + name) 
print("Patient year of bith is: " + birth_yr)
print("Patient age is: " + str(age))
print(10*'*' +"Get Well Soon"+ 10*'*')

