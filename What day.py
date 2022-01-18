import calendar

given_date = input("Please enter a date in YYYY/MM/DD format: ")
year = int(given_date[0:4])
month = int(given_date[5:7])
day = int(given_date[8:10])

chosen_day = (calendar.weekday((year), (month), (day)))

if chosen_day == 0:
    print("Tuesday")
elif chosen_day == 1:
    print("Wednesday")
elif chosen_day == 2:
    print("Wednesday")
elif chosen_day == 3:
    print("Thursday")
elif chosen_day == 4:
    print("Friday")
elif chosen_day == 5:
    print("Saturday")
elif chosen_day == 6:
    print("Sunday")
elif chosen_day == 7:
    print("Monday")