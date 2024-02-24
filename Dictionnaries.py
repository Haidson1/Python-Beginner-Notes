
'''
Uses the principle of an actual dictionary: Word : Definition
The Word is a "Key" - the Definition is the "Value"
 "Key": Value (add a , at the end if your dictionary has multiple entries)
'''

dictionaryExample = {
    "FirstValue": "A", #Needs a "," after each row to prevent errors
    "SecondValue": True,
    "ThirdValue": 3
}

print(dictionaryExample["FirstValue"])

if dictionaryExample["SecondValue"] is False:
    print(str(dictionaryExample["SecondValue"]))
else:
    print("Value is True")

print(dictionaryExample.get("First", "Value to pass if turns to be invalid"))