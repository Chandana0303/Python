'''import time

#no. of ticks
t=time.time()
print(t)

#complete date/time info
d=time.localtime()
print(d)

#format date/time
s=time.asctime()
print(s)
'''
import calendar

c = calendar.month(2021, 8)
print(c)

import datetime

d= datetime.datetime.now()
print(d)
print(d.year)
print(d.month)
print(d.date())
print(d.hour)
print(d.minute)
print(d.second)