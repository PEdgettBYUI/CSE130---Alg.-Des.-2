# 1. Name:
#      Patrick T. Edgett
# 2. Assignment Name:
#      Lab 06: Image Compression
# 3. Assignment Description:
#      This is a program to take a JSON file and decompress it into a
#       Mono-tone image using ASCII characters and display it on screen
# 4. Algorithmic Efficiency
#      The Big O of the program is O(n*m), this is because the efficiency of the program is
#       determined by the size of the image being decompressed, specifically, how many
#       rows and columns it takes up.
# 5. What was the hardest part? Be as specific as possible.
#      Aside from the Pseudocode, which was a struggle to wrap my head around the logic of,
#       the hardest part was trying to understand what each nested for loop actually dictated
#       and following that logic as I developed the program. I have submitted this assignment late,
#       and honestly, even with the solutions present to fact check against, I still had a hard time wrapping
#       my head around how to accress the 2D array and add things to it. I think I might still be overthinking it,
#       but honestly, it still doesn't make complete sense to me even as I write this following testing the program.
# 6. How long did it take for you to complete the assignment?
#      PseudoCode: 6hrs + Actual code: 2hrs = ~8hrs

import json



def read_data_from_json(filename):
    try:
        with open(filename, "rt") as filehandle:
            file_data = filehandle.read()
            json_data = json.loads(file_data)
            return json_data
    except:
        print("Unable to open file " + filename + ".")
    

# "main()"
print("Welcome to the Image decompressor.")
userinput = input("Type the filename/path you want to open: ")   # May need to include path from root

raw_data = read_data_from_json(userinput)

num_rows = raw_data["num_rows"]
num_columns = raw_data["num_columns"]
img_data = raw_data["data"]

# Initialize 2D array
print(f"{num_rows},\n\n{num_columns},\n\n{img_data}\n") # Test Print

decodedImg = []
for i_row in range(num_rows):
    decodedImg.append([])
    # print(i_row)  // Test Message

# "For each column..."
for i_column in range(num_columns):
    # Initialize row index and boolean tracker
    black = True
    i_row = 0

    # "For each set of numbers in a row..."
    for set in img_data[i_column]:
        for set_vals in range(set):
            if black:
                decodedImg[i_row].append("*")
                i_row += 1
                assert i_row <= num_rows
            else:
                decodedImg[i_row].append(" ")
                i_row += 1
                assert i_row <= num_rows
        black = not black

print("\n\n")   # Spacing for readability

# Display image
for row in decodedImg:
    for pixel in row:
        print(pixel, end='')
    print()
print()