import datetime
from datetime import date

print("-"*50)
print(" "*10+"Birthday App"+" "*10)
print("-"*50)
birthyear = int(input("What year were you born [YYYY]? "))
birthmonth = int(input("What month were you born [MM]? "))
birthday = int(input("What day were you born [DD]? "))

print("It looks like you were born on %s/%s/%s" %(birthmonth,birthday,birthyear))
today = datetime.date.today()
future = date(2017,10,20)
diff =  future - today
print("Looks like your birthday is in %s days"%(diff.days))
print("Hope you're looking forward to it!")
