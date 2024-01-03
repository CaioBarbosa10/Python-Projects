
try:
    file = open("a_file.txt")
    a_dictionary = {
        "key": "value"
    }
    print(a_dictionary["asjaisjai"])
except FileNotFoundError:
    file = open("a_file.txt","w")
    file.write("Somenthing")