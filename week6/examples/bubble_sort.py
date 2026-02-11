import random

def bubble_sort(numbers):
    for i in range(len(numbers) - 1, 0, -1):
        for j in range(0, i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                print(numbers)

def create_random_numbers_list(size):
    random_numbers = []
    for i in range(size):
        random_numbers.append(random.randint(0, 1000))
    return random_numbers

def main():
    data = [1, 3, 9, 3, 2, -1, 10, 9, -4, 7]
    bubble_sort(data)
    print(data)

    numbers = create_random_numbers_list(16)
    bubble_sort(numbers)
    print(numbers)

main()