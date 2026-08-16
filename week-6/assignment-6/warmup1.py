
def greet(name, greeting = "Hello"):
    print( greeting + "," + " " + name + "!" )


greet("Alex") # With only a name argument

greet("Alex","Good morning") # With both a name and a custom greeting

greet("Alex", greeting = "Hello") # With the greeting passed as a keyword argument