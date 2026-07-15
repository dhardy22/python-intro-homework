# Write a program that asks the user for a day of the week and a time of day (morning, afternoon, or evening), then suggests an activity.

# Requirements:
# Cover at least 3 days × 3 times = 9 combinations with distinct suggestions
# Handle any unrecognized day or time with a friendly fallback message
# Normalize input so capitalization doesn't matter (e.g., "Monday" and "monday" both work)

#User inputs for day and time of day
day_of_week = input("What day is it?: ").casefold()
time_of_day = input("What is the time of day?: ").casefold()


#Monday suggestions
if day_of_week == "monday" and time_of_day == "morning" :
    print("Enjoy a slow morning - Mondays can get crazy")

if day_of_week == "monday" and time_of_day == "afternoon" :
    print("Refuel with coffee or tea!")

if day_of_week == "monday" and time_of_day == "evening" :
    print("Relax, You survived another Monday!")


#Friday suggestions
if day_of_week == "friday" and time_of_day == "morning" :
    print("“Hey Siri, Play Friday (Dopamine Re-Edit)”")

if day_of_week == "friday" and time_of_day == "afternoon" :
    print("Wrap up and log off!")

if day_of_week == "friday" and time_of_day == "evening" :
    print("The couch is calling you. I’m not judging")


#Saturday suggestions
if day_of_week == "saturday" and time_of_day == "morning" :
    print("Get some exercise!")

if day_of_week == "saturday" and time_of_day == "afternoon" :
    print("Check out the farmers market")

if day_of_week == "saturday" and time_of_day == "evening" :
    print("Go out on the town")
else :
    print("Sorry, I don't recogize that day or time of day. Try entering Monday, Friday, or Saturday; Morning, Afternoon, or Evening")


