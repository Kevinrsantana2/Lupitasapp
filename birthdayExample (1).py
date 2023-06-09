# Kevin Ruiz Santana 2023
import json
# this is a relative path to the .json data file
# pathToFile = "birthday (1).json"
#relative path to file
pathToFile = "birthday (1).json"

# try to open a file and throw a error if it is not found
try:
    jsonFile = open(pathToFile, 'r')
except OSError:
    print("ERROR: Unable to open the file %s" % pathToFile)
    exit(-1)


# read the whole json file into a variable
birthdayList = json.load(jsonFile)

# create an empty dictionary
birthdayDictionary = {}

nameFind = input("Enter a name:")
print("The name the user entered is: " + nameFind)
# print("ENTERING THE LOOP\n")

# loop json list of data and put each name and birthday into a dictionary
for elem in birthdayList:

    # fetch name and birthday
    name = elem["name"]
    birthday = elem["birthday"]

    # print("name = " + name)
    # print("birthday = " + birthday)

    birthdayDictionary[name] = birthday

if birthdayDictionary.get(nameFind):
    print("\nThe name " + nameFind + " was found and the birthday is: " + birthdayDictionary.get(nameFind))
else:
    print("Lupe does not have any friends that match that name " + nameFind) 

# to print a value in the dictionary by giving it a string with the name as the key
# print("Jocelyn Jones's birthday is: " + birthdayDictionary["Jocelyn Jones"])