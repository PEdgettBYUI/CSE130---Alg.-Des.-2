import math # For is_prime

number = int(input("Provide a number: "))

# # for look of power
# power = 1
# for i in range(number):
#     power *= 2
#     print(power)


# while version of Power
power = 1
iterator = 0
print(1)    # Any number to the 0th power = 0
while iterator != number:
    power *= 2
    print(power)
    iterator +=1

#--------------------------------------------------------------------------#

# # Stars loop
pyr_height = 15

for i in range(1, pyr_height, 2):
    print()
    print(' ' * ((pyr_height - i) // 2), end='') # makes number of spaces
    for j in range(1, i+1):
        print("*", end='')
print()
print()

#--------------------------------------------------------------------------#

# # Is Prime Number

def is_prime(number):
    for n in range(2, int(math.sqrt(number)) + 1):
        if number % n == 0:
            return False
        return True
    
for i in range(1, 20):
    if is_prime(i):
        print(i)

