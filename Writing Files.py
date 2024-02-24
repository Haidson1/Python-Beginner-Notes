
# --------- Appending to bottom of the file ---------
theFile = open("readWriteFile.txt", "a") # Append Mode

theFile.write("\nAppending bottom line") # Will write a new line at the bottom of the file as the file is opened with Append

theFile.close()

# --------- Overriding the existing content of the file ---------
theFile = open("readWriteFile.txt", "w") # Write Mode

theFile.write("Overriding existing content") #The content within "write" is the entirety of the file, getting rid of everything else

theFile.close()

# --------- Creating a new file ---------
theFile = open("ANewFile.txt", "w") # Write mode on non-existing file

theFile.write("Content within your new file")

theFile.close()

