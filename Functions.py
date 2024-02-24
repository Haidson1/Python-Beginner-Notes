
# --------- Basic Function execution ---------
def aBasicFunction():
    print("Here's the values within your function")

aBasicFunction() #executes the code


# --------- Function requiring a value ---------
def aFunctionWithArgument(value):
    print("Here's the value you added: " + value)

aFunctionWithArgument("The defined value") #Executing the function, passing the value


# --------- Function requiring multiple values ---------
def functionWithMultipleArguments(firstValue, secondValue):
    print("My string value: " + firstValue + " my second value (int): " + str(secondValue))

functionWithMultipleArguments("Something", 999)

# --------- Function with used argument ---------
def someWildFunction(someVariable):
    print(f'Good morning {someVariable}!')
someWildFunction("Nicolas")