# check if day is weekday or weekend by date
# Author: Sadie Concannon

import datetime

# to get the number of the weekday
weekNumber = datetime.datetime.today().weekday()

if weekNumber < 5:
    print ("Today's DateTime is {0} and it's a Weekday".format(datetime.datetime.today()))
else:
    print ("Today's DateTime is {0} and it's the Weekend, Yay".format(datetime.datetime.today()))
    
