number = int(input('Please input a number: '))

numbers = []
import random
for i in range(number):
    numbers.append(random.randrange(0, number * 10))

found = False
duplicates = []

for index_1 in range(number):
    for index_2 in range(index_1 + 1, number):
        loop_count += 1
        if numbers[index_1] == numbers[index_2]:
            found = True
            duplicates.append(numbers[index_1])

if found:
    print(f'There is a duplicate in the array: {numbers}')
    print(f'The duplicate numbers are: {duplicates}')
else:
    print(f'There are no duplicates in the array: {numbers}')