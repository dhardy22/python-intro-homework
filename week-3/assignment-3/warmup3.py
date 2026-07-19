result_1 = not True and False
print(f"not True and False: {result_1}") # Because not True is False. False and False is False because AND requires both statements to be True") # not True is False. False and False is False because AND requires both statements to be True

result_2 = True or False and False
print(f"True or False and False: {result_2}") # Because AND is evaluated first so False and False is False. OR requires one of the values to be True so it True

result_3 = not (5 > 3) 
print(f"not (5 > 3): {result_3}") # Because 5 is greater than 3 is True. not True is False

result_4 = 10 == 10 and 4 != 4 
print(f"10 == 10 and 4 != 4: {result_4}") # Because 10 is equivalent to 10 is True. 4 not equal to 4 is False. AND requires both statements to be True so it is False

result_5 = not False or not True
print(f"not False or not True: {result_5}") # Because not False is True. not True is False. For OR only one condition has to be True so it is True

