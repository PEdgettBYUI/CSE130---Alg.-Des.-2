# 1. Name:
#      -Patrick T. Edgett-
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      -This program is a simple authenticator, in which the user provides a Username and Password, which is compared against a linked-list in authenticator.json. If the Username and Password provided match the Indexes in the Linked list, you're allowed access, if not you are denied access-
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of the assignment was opening and reading the JSON file, as I haven't worked with JSON for awhile, and I had some difficulty recalling how to interact with the file.
#      I borrowed some code from a classmate about opening the file, and asked ChatGPT for help on converting the JSON sting into a dictionary. From there, I knew what I needed to do, but got some additional help from Brother Godderidge.
#      He reminded me that the json library and json.loads would convert the string into a dictionary, which I could then use to create my lists for username and password.
#      After that, the rest of the assignment was fairly straightforward.
# 5. How long did it take for you to complete the assignment?
#      The assignment took me roughly 2-4 hours to complete. This includes breaks, research, and asking for help.


import json

# Convert the JSON to a list
filename = "week2/authenticator.json"

# NOTE: While loop for demonstration purposes, exit by entering exit as username
input_username = "blank"
while input_username != "exit":

    try:
        with open(filename, "r") as file:
            data_text = file.read() # <-- The JSON is a raw String

        # print("JSON as string:")
        # print(data_text)

        # Turns string into a python object
        # Converts it into a dictionary
        data_dictionary = json.loads(data_text)
        # print(data_dictionary["username"])
        # print(data_dictionary["password"])

    # Create two lists from the dictionary entries
        user_dict = data_dictionary["username"]
        pass_dict = data_dictionary["password"]

    except Exception as e:
        print(f"unable to open file {filename}: {e}")

    # Prompt for Username
    input_username = input("Enter your username: ")

    # Prompt for Password
    input_password = input("Enter your password: ")

    # Check if username and password match the correct entries in the linked-list
    print()
    if input_username in user_dict:
        index = user_dict.index(input_username)
        if input_password == pass_dict[index]:
            print("You are authenticated!")
        else:
            print("You are not authorized to use the system.")
    else:
        print("You are not authorized to use the system.")
    print()