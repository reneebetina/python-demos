from datetime import datetime  #to get datetime NOW
import pandas as pd #for more date operations
import pytz # for timezone details

current_time = datetime.now()
time_stamp = current_time.timestamp()
#print("timestamp:-", time_stamp)
date_time = datetime.fromtimestamp(time_stamp)

# Time formatting

print("*** SHOW CURRENT DATE TIME ***")
str_date = date_time.strftime("%B %d %Y %I:%M:%S %p")
print("Format 1 (AM/PM): ", str_date)


str_date = date_time.strftime("%B %d %Y %H:%M:%S")
print("Format 2 (-24H-): ", str_date)

str_date = date_time.strftime("%m %d %y %H:%M:%S")
print("Format 3 (Custom): ", str_date)

str_date = date_time.strftime("%Y-%m-%d %I_%M_%S%p")
print("Format 4 (Custom): ", str_date)


print("\n*** MORE DETAILS ***")
print("Show Day of Week (0=Sunday, 1=Monday ...)")
print("\t\tToday is a {}".format(date_time.strftime('%A')) )
print("\t\tToday is a {}".format(date_time.strftime('%a')) )
print("\t\tToday is a {}".format(date_time.strftime('%w')) )

print("Week # {} of this year ".format(date_time.strftime('%W')) )

print("\n*** SHOW TIMEZONE ***")
unaware = datetime.now()
print('Timezone naive:', unaware)

# Standard UTC timezone aware Datetime
aware = datetime.now(pytz.utc)
print('Timezone Aware:', aware)
print("\tTimezone: {}".format(aware.strftime('%z')) )
print("\tTimezone: {}".format(aware.strftime('%Z')) )

print("\n*** DATE TIME OPERATIONS using Pandas ***")

year = int(date_time.strftime("%Y"))
month = int(date_time.strftime("%m"))
day = int(date_time.strftime("%d"))
hours = int(date_time.strftime("%H"))
mins = int(date_time.strftime("%M"))
seconds = int(date_time.strftime("%S"))

dtDate = datetime(year,month,day,hours,mins,seconds)
print ("TODAY: ",dtDate)
print ("Last Year: ",dtDate - pd.DateOffset(years=1))
print ("Last Month: ",dtDate - pd.DateOffset(months=1))
print ("Next Month: ",dtDate + pd.DateOffset(months=1))
print ("Next 9 Months: ",dtDate+ pd.DateOffset(months=9))


current_year =  datetime.now().strftime("%Y")
# birthday
full_birthdate = datetime(1993,4,22,0,0)
birth_month = full_birthdate.strftime("%m")
birth_day = full_birthdate.strftime("%d")

difference = dtDate - full_birthdate
#print(difference)
print("I was born on {}. Today I'm {} days old".format(full_birthdate, difference.days))
print("I am {} years old".format(difference.days//365)) # // to get full number only
current_byear = datetime(int(current_year), int(birth_month), int(birth_day))
next_byear = current_byear + pd.DateOffset(years=1)

print("NEXT Birthday: ", next_byear)

print("Countdown: ", next_byear - dtDate)
