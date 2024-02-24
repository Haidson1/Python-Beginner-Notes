
# --------- For loop in a string ---------
for letter in "This is a string of words":
    print(letter)

# --------- For loop in an array ---------
anArray = ["A", "B", "C"]
for items in anArray:
    print(items)

# --------- For loop using the length value (int) of an array ---------
for i in range(len(anArray)):
    print(i+1) #prints index "i" for the length of anArray +1 (1,2,3)

# --------- For loop using a range ---------
for i in range(3,10):
    print(i) #Prints (included, excluded) (3,4,5,6,7,8,9)

# --------- For loop using an index value (int) ---------
for index in range(10):
    if index == 3:
        print("Fourth iteration of the loop")
