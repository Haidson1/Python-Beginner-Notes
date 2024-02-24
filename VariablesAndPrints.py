
#Variable Types
StringVariable = "A String"
IntegerVariable = 10
DoubleVariable = 1.14975
boolVariable = False

#Console Prints
print("This is a print function")
print("This prints with a \n return (putting it on 2 lines)")

#Working with Strings
print("Can show a variable AND string " + str(IntegerVariable))
print("You can also set functions on String variable, such as " + StringVariable.lower())
print("Show how many characters are in the string: " + str(len(StringVariable)))
print("Get the positional index value within a string: " + StringVariable[4])
print("Get the index ID of a character within a string: " + str(StringVariable.index("n")))
print("Replace the value of a variable by another: " + StringVariable.replace("String", "STRING OF CHARACTERS"))

#Working with Ints/Doubles
InitialDouble = 10.15
AbsoluteValue = abs(InitialDouble)
PowerValue = pow(3,2) #3 to the Square of 2 (3x3)
MaximumValue = max(5,10) #Will give the maximum value between the 2 values provided (good when using arrays or variables)
MinimumValue = min(5,10) #Will give the minimum value between the 2 values provided (good when using arrays or variables)
RoundedValue = round(3.12) #Will round the value