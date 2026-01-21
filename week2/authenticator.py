# 1. Name:
#      -Patrick T. Edgett-
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      -This program is a simple authenticator, in which the user provides a Username and Password, which is compared against a linked-list in Lab02.json. If the Username and Password provided match the Indexes in the Linked list, you're allowed access, if not you are denied access-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-


import json

# Convert the JSON to 2 Lists
filename = "week2/authenticator.json"

try:
    with open(filename, "r") as file:
        data_text = file.read() # <-- The JSON is a raw String

    print("JSON as string:")
    print(data_text)

    # Turns string into a python object
    # Converts it into a dictionary
    data_dictionary = json.loads(data_text)
    print(data_dictionary["username"])
    print(data_dictionary["password"])



except Exception as e:
    print(f"unable to open file {filename}: {e}")



# Prompt for Username
# Prompt for Password
# 