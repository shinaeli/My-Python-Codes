time_now = input("enter time now: ")
int(time_now)
number_of_hours_to_wait = input("enter number of hours to wait: ")
int(number_of_hours_to_wait)
number_of_days = int(number_of_hours_to_wait)//24
int(number_of_days)
number_of_hours_left = int(number_of_hours_to_wait)%24
int(number_of_hours_left)
exact_hour_of_alarm = int(time_now)+int(number_of_hours_left)
int(exact_hour_of_alarm)
exact_time_of_alarm = int(exact_hour_of_alarm)-12
int(exact_time_of_alarm)
print(exact_time_of_alarm)
print("The alarm will go off 2days later, in the evening at exactly", exact_time_of_alarm)

