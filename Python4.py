##Create a file (samplefile.txt) on your machine manually and note the path of the file. 

file = open("<file path of samplefile.txt>", "a")
file.write("New customer Bank of London was added successfully")
file.close()

#open and read the file after the appending:
f = open("samplefile.txt", "r")
print(f.read())
