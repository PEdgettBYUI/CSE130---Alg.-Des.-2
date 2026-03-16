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


def bubsy_sort(array):    # "What could possibly go wrong?" ~ 90's Bobcat ltd
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(array)-2):
            if array[i] > array[i+1]:
                array[i] = array[i+1], array[i+1] = array[i]
                swapped = True
    return array

#-----------------------------------------------------------------------------------------------#

u_input = input("Provide a filename/path to read from: ")

raw_data = read_data_from_json(u_input)
raw_data = raw_data["array"]

print(f"The Unsorted File contents are as follows: \n\n{raw_data}\n\n")

print("Applying 'bubsy sort'...")




