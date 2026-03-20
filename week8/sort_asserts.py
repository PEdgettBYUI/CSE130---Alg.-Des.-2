# 1. Name:
#      Patrick T. Edgett
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program is a bubble sort that demonstrates the use of asserts
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was figuring out how to implement the asserts. Some of the errors
#       weren't obvious, and even the ones that were, such as making sure the file exists
#       or that it ends with a ".json". I eventually looked up and decided to use the "os"
#       library to achieve that function, and it appears to work. Sometimes it was difficult
#       to discern what should be considered a potential error or not, such as if having an
#       empty array be accepted or not. I ultimately decided not, as it made no sense to try and
#       sort an array with nothing to sort.
#       
# 5. How long did it take for you to complete the assignment?
#      About 4 hours I think?
import json
import os

# # This function takes the path and filename of the file from the room folder of the program
# # and will return all of the json data as a dictionary that can be stored elsewhere
def read_data_from_json(filename):
        assert os.path.isfile(filename), "file does not exist"

        with open(filename, "rt") as filehandle:
            file_data = filehandle.read()
            json_data = json.loads(file_data)
            return json_data

# # The "bubsy sort" is a lazy sort, that will slowly go through an array and swap each
# # adjacent value with each other. What makes it lazy is it defaults to ASCII values
# # for non-numeric characters. Meaning that capital letters always appear before lowercase
# # letters, even if it doesn't make much sense linguistically.
def bubsy_sort(array):    # "What could possibly go wrong?" ~ 90's Bobcat ltd
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(array)-1):
            assert i >= 0 < len(array)-1, "Out of bounds"   # Uesless assert???
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
    assert sorted(array) == array, "Array not sorted"
    return array

#-----------------------------------------------------------------------------------------------#

u_input = input("Provide a filename/path to read from: ")
assert u_input.endswith(".json"), "does not end with '.json'"

raw_data = read_data_from_json(u_input)

raw_data = raw_data["array"]
# raw_data2 = raw_data    # TEST: for Sorted() assert comparison
assert raw_data, "The array is Empty and cannot be sorted"

# print(f"The Unsorted File contents are as follows: \n\n{raw_data}\n\n")

print("Applying 'bubsy sort'...")

sorted_data = bubsy_sort(raw_data)
# sorted_data2 = sorted(raw_data2)    # TEST: for Sorted() assert comparison
print(f"The Sorted Array:")

for item in sorted_data:
    print(f"    {item}")
print("\n\n")

# # # TEST: Visual comparison for Sorted() assert
# for item in sorted_data2:
#     print(f"    {item}")
# print("\n\n")