
isTrue = True
isAValue = False

# --------- Basic if statement ---------
if isTrue:
    print("Value is true")
else:
    print("Value is false")

# --------- If statement with and/or conditions ---------
if isTrue and isAValue:
    print("Both values true")
else:
    print("Not both values true")

if isTrue or isAValue:
    print("One of both values true")
else:
    print("No values true")


# --------- If statement with else if conditions ---------
if isAValue:
    print("Value is true")
elif isTrue:
    print("A value not true but isTrue is")
else:
    print("No value true")
