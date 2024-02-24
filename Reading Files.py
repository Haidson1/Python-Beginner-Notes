
'''
Working with files:
r : Read-Only
r+ : Read & Write (full access)
w : Write to file
a : Append to a file (add at the end of the file, cannot update existing)
'''

storingFile = open("readWriteFile.txt", "r") #Open the file in Read Only and push all the data from file in storingFile

if storingFile.readable(): #Ensure we can read the file prior to operating on it
    
    print(storingFile.read()) #Print the whole file

    print(storingFile.readline()) #Reads the first line, and will read the next index after each iteration

    print(storingFile.readlines()) #Converts each lines as an index within an array.




storingFile.close() #Ensure we are no longer accessing the file once we're done working with it
