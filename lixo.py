from datetime import date
d0 = date(2011, 1, 8)
d1 = date(2015, 8, 16)
delta = d1 - d0
print('The number of days between the given range of dates is :')
print(delta.days)