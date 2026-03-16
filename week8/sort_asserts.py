# 1. Name:
#      Patrick T. Edgett
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program is a bubble sort that demonstrates the use of asserts
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-
import json



def read_data_from_json(filename):
    try:
        with open(filename, "rt") as filehandle:
            file_data = filehandle.read()
            json_data = json.loads(file_data)
            return json_data
    except:
        print("Unable to open file " + filename + ".")