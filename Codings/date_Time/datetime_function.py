import datetime

curr_date = "7/1/22"
curr_date_temp = datetime.datetime.strptime(curr_date, "%m/%d/%y")

new_date = curr_date_temp - datetime.timedelta(days=1,hours=3)
print(new_date)