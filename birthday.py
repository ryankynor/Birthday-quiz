"""
birthday.py
Author: Ryan Kynor
Credit:
http://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/

Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""


from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
month2 = month_name[todaymonth]

## Only date representation
#print ("Current date "  + time.strftime("%x"))


name = input("Hello, what is your name? ")
month = input("Hi {0}, what was the name of the month you were born in? ".format(name))
year = input("And what year were you born in, {0}? ".format(name))
day = input("And the day? ")

if month == "October" and int(day) == 31:
    print ("You were born on Halloween!")

    
if year<="1999" and year>="1990":
    yearage = "nineties."
if year<="1989" and year>="1980":
    yearage = "eighties."
if year>="2000":
    yearage = "two thousands."
if year<"1980":
    yearage = "stone age."


if month == month_name[todaymonth] and int(day) == todaydate:
    print ("Happy birthday!")
elif month == "December" or "January" or "Febuary":
    print ("{0}, you are a winter baby of the {1}".format(name, yearage))
elif month == "March" or "April" or "May":
    print ("{0}, you are a spring baby of the {1}".format(name, yearage))
elif month == "June" or "July" or "August":
    print ("{0}, you are a summer baby of the {1}".format(name, yearage))
else:
    print ("{0}, you are a fall baby of the {1}".format(name, yearage))
