
print(not True and False)  # Because not True is False. False and False is False because AND requires both statements to be True  
print(True or False and False)  # Because AND is evaluated first so False and False is False. OR only requires one variable to be True
print(not (5 > 3))    # Because 5 is greater than 3 is True. not True is False
print(10 == 10 and 4 != 4)  # Because 10 is equivalent to 10 is True. 4 not equal to 4 is False. AND requires both operands to be True so it is False
print(not False or not True)  # Because not False is True. not True is False. For OR only one condition has to be True so it is True


