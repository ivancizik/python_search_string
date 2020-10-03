# https://github.com/ivancizik/python_search_string

search_term = "The quick brown fox jumps over the lazy dog"

search_input = ""
offset = 0
search_results = ""

print(">>>Search term is:", search_term)

print(
    '''
    Use the following search functions:
    string      = check is searched item is a match
    *string     = check is searched item ends with string
    string*     = check is searched item starts with string
    *string*    = check is searched item contains with string
    -x          = search parameter
    '''
    )

while True:  # making a loop
    search_input = input("Add search input: ")
    print("")

    if search_input == "": # Now that's what i call a pro gamer move
        search_input = "   "
    

    if search_input[-2:] == "-x":
        print("-x = search parameter detected")
        offset = 3
        search_parameter = "You used search parameter"

    if search_input[0] == "*" and search_input[-1 - offset] == "*":
        print("*string* = contains parameter detected")
        search_results = search_input.split("*")[1].lower() in search_term.lower()
        print("Search input:", search_input.split("*")[1])
        print("")

    else:
        print("no special parameter detected (default), using ==")
        search_results = search_input.split(" -")[0].lower() == search_term.lower()
        print("Search input:", search_input.split(" -")[0])
        print("")

        if search_input[0] == "*":
            print("*string = ends with parameter detected")
            search_results = search_term.lower().endswith(search_input.split("*")[1].split(" -")[0].lower())
            print("Search input:", search_input.split("*")[1].split(" -")[0])
            print("")

        if search_input[-1 - offset] == "*":
            print("string* = starts with parameter detected")
            search_results = search_term.lower().startswith(search_input.split("*")[0].lower())
            print("Search input:", search_input.split("*")[0])
            print("")

    offset = 0 # reset to 0 in in loop
    print("")
    print("Did we foud what we were looking for?: ", search_results)
    print("True = yes, False = no")
    print("")

    if search_results == True:
        print("We found it, executing code...", search_parameter)
        print(search_term)
        print("")
