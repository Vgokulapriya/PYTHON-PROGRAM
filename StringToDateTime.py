from datetime import datetime

my_date_string = "FEB 13 2022 10:30AM"

datetime_object = datetime.strptime(my_date_string, "%b %d %Y %I:%M%p")

print(type(datetime_object))
print(datetime_object)
