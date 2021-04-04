def is_leap(year):
  """Test if a year is leap."""
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

def days_in_month(y, m):
  """Return how many days in a month of a specific year.\n
  Takes into account leap years."""
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if m > 12 or m < 1:
    return "ERROR!"
  if m == 2 and is_leap(y):
    return 29
  return month_days[m-1]

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)





