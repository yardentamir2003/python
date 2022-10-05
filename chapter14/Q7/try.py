from datetime import datetime, time
from datetime import date

today = date.today()

str_d1 = '2021/10/20'
str_d2 = '2022/2/20'

d1 = datetime.strptime(str_d1, "%Y/%m/%d")
d2 = datetime.strptime(str_d2, "%Y/%m/%d")

delta = d2 - d1
print(f'Difference is {delta.days} days')


