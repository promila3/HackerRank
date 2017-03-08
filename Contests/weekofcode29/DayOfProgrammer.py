#!/bin/python

import sys
import datetime




y = int(raw_input().strip())
DAY_OF_YEAR = 256
YEAR = y
if y == 1918:
    DAY_OF_YEAR += 14
d = datetime.date(YEAR, 1, 1) + datetime.timedelta(DAY_OF_YEAR - 1)
#print dt
#print '{0}.{1}.{2:02}'.format(dt.day, dt.month,  dt.year)
print datetime.date.strftime(d, "%d.%m.%Y")
# your code goes here
