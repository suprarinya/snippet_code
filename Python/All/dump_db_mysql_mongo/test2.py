import datetime

d = datetime.date(2012, 9, 1)
print (type(d) is datetime.date)

print(d)

def convert_date_todatetime(date):
    return datetime.datetime.combine(date, datetime.time.min)


dt = convert_date_todatetime(d)
print(dt)
