# Write a program that asks the user for a day of the week and a time of day (morning, afternoon, or evening), then suggests an activity.

# Requirements:
# Cover at least 3 days × 3 times = 9 combinations with distinct suggestions
# Handle any unrecognized day or time with a friendly fallback message
# Normalize input so capitalization doesn't matter (e.g., "Monday" and "monday" both work)

#User inputs for day and time of day
day_of_week = input("Enter a day of the week: ").casefold().strip()
time_of_day = input("Enter a time of day: ").casefold().strip()

#contains all of the valid days contained in valid days and valid times
valid_days = ("monday", "friday", "saturday")
valid_times = ("morning", "afternoon", "evening")

#this block checks for the valid response inside of valid days and valid times
if day_of_week not in valid_days and time_of_day not in valid_times:
    print("I don't recognize either your day or your time. Try Monday, Friday, or Saturday; Morning, Afternoon, or Evening.")
elif day_of_week not in valid_days:
    print("I don't recognize that day. Try Monday, Friday, or Saturday.")
elif time_of_day not in valid_times:
    print("I don't recognize that time. Try Morning, Afternoon, or Evening.")
else:
    
#Monday suggestions
    if day_of_week == "monday" and time_of_day == "morning" :
        print("Suggestion: Enjoy a slow morning! - Mondays can get crazy")

    elif day_of_week == "monday" and time_of_day == "afternoon" :
        print("Suggestion: Refuel with coffee or tea!")

    elif day_of_week == "monday" and time_of_day == "evening" :
        print("Suggestion: Relax, You survived another Monday!")

    #Friday suggestions
    elif day_of_week == "friday" and time_of_day == "morning" :
        print("Suggestion: “Hey Siri, Play Friday (Dopamine Re-Edit)!”")

    elif day_of_week == "friday" and time_of_day == "afternoon" :
        print("Suggestion: Wrap up and log off!")

    elif day_of_week == "friday" and time_of_day == "evening" :
        print("Suggestion: The couch is calling you. I’m not judging")

    #Saturday suggestions
    elif day_of_week == "saturday" and time_of_day == "morning" :
        print("Suggestion: Get some exercise!")

    elif day_of_week == "saturday" and time_of_day == "afternoon" :
        print("Suggestion: Check out the farmers market!")

    elif day_of_week == "saturday" and time_of_day == "evening" :
        print("Suggestion: Go out on the town!")
   

# print(repr(day_of_week), repr(time_of_day))
