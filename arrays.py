
Alphabet = ["Alpha", "Bravo", "Charlie"]
Numbers = [1, 2, 3, 4, 5]
print(Alphabet) #Prints the whole thing: including brackets, commas and ' ' next to values
print(Alphabet[1]) #Print the value at Index 1 (in this instance: Bravo)
print(Alphabet[1:]) #Prints all the elements at Index 1 and after
print(Alphabet[0:2]) #Prints all elements from Index 0 up to EXCLUDED 2
Alphabet[1] = "Delta" #Will update the value at Index 1 to new defined value

Alphabet.append(Numbers) #Will add the data from Numbers at the end of the list
Alphabet.append("Echo") #Will add "Echo" at the end of the Alphabet list
Alphabet.insert(1, "Second Alpha") #Adds value at the index position 1, everything else pushed off to the right
print(Alphabet.index("Bravo")) #Will print the index at which "Bravo" can be found
Alphabet.remove(Alphabet[1]) #Remove value at position 1
Alphabet.sort() #Sort the list in ascending order
Alphabet.pop() #Removes the last value of the list
Alphabet.clear() #Wipes the whole list

Alphabet_copy = Alphabet.copy() #Copies all the context of the list in a new list


