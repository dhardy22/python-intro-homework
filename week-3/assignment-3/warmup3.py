
print(not True and False)  # Because "not" is evaluated first so not True is False. False and False is False because AND requires both statements to be True for the expression to be True.  
print(True or False and False)  # Because AND is evaluated first between "AND" and "OR" so False and False is False. OR only requires one variable to be True for the expression to be True. 
print(not (5 > 3))    # Inequalities are evaluated before Boolean operators so 5 is greater than 3 is True. not True is False
print(10 == 10 and 4 != 4)  # Comparison operators are evaluated before Boolean operators so 10 is equivalent to 10 is True. 4 not equal to 4 is False. AND requires both operands to be True so it is False
print(not False or not True)  # "not" is evaluated first so not False is True. not True is False. OR only one condition has to be True for the expression to be True


