# functions with outputs

def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  Name = f_name.title() + " " + l_name.title()
  #Name2 = (f_name + l_name).title()
  return Name

print(format_name("oBaDa", "EiD"))

############################
#Instructions
# Convert the is_leap() functtion
# In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

# Create a new function called days_in_month()
# You are then going to modify a function called days_in_month() which will take a year and a month as inputs
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
       return True
      else:
        return False
    else:
       return True
  else:
    return False

# TODO: Add more code here 👇
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if is_leap(year) == True and month == 2:
    return 29
  else: 
    return month_days[month-1]


#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

