# 1. Name:
#      Patrick T. Edgett
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      This program determines if during a given turn the player can obtain a hotel on pennsylvania avenue.
# 4. What was the hardest part? Be as specific as possible.
#      It has been awhile since I've made a program like this in python. Admittedly, there are far too many questions, and the process by which it is determined if the program can continue or end is cumbersome and complex for what it does. I tried to stay close to the intended prompts and outputs, but was unable to do so efficiently, and the purchase case outputs are very different from the example. Bug testing was also difficult. I checked every case manually to ensure that it worked properly, which took a lot of extra time.
# 5. How long did it take for you to complete the assignment?
#      Approx. 5-6hrs, including the time to design the flow chart & refine it.



def set_variables():
    global cash, bank_houses, bank_hotels

    print("\nWhat is on North Carolina Avenue? \n(0:nothing, 1-4: # of Houses, 5:a hotel)")
    g_prop["North Carolina Ave"] = int(input("Enter 1-5: "))

    print("\nWhat is on Pacific Avenue? \n(0:nothing, 1-4: # of Houses, 5:a hotel)")
    g_prop["Pacific Ave"] = int(input("Enter 1-5: "))

    print("\nWhat is on Pennsylvania Avenue? \n(0:nothing, 1-4: # of Houses, 5:a hotel)")
    g_prop["Pennsylvania Ave"] = int(input("Enter 1-5: "))

    cash = int(input("\nHow much cash do you have to spend? "))

    bank_houses = int(input("\nHow many houses are there to purchase? "))

    bank_hotels = int(input("\nHow many hotels are there to purchase? "))
    print("\n------------------------------------------------------\n")


# Determines if you can afford to purchase the houses needed before buying a hotel
def afford_buildings(houses_needed, user_cash):    
    # print(houses_needed)
    # print(user_cash)
    remainder = 0
    total_price = (houses_needed * 200)

    if user_cash > total_price:
        print("[You Buy all the Necessary Houses]")
        user_cash = user_cash - total_price
    else:
        print("[You do not have sufficient funds to purchase a hotel at this time.]")
        return 'n'  # Used to tell program to End


def swap_hotels():
    if g_prop["North Carolina Ave"] == 5 or g_prop["Pacific Ave"] == 5:
    
        swap = str(input("You have enough hotels to swap to PA Avenue, would you like to?(y/n) "))
        if swap.lower() == 'y':
            if g_prop["North Carolina Ave"] == 5:
                print("[Swap North Carolina's hotel with Pennsylvania's 4 houses.]")
                return 'y'  #   You swapped Hotels
            elif g_prop["Pacific Ave"] == 5:
                print("[Swap Pacific's hotel with Pennsylvania's 4 houses.]")
                return 'y'  #   You swapped Hotels
        else:
            print("[You do not swap any Hotels.]")
            return 'n'  # You did not swap

    else:
        print("[You did not Swap, you have no Hotels.]")
        return 'n'  # You did not swap






# Number of buildings on a given property.
g_prop = {
    "North Carolina Ave": 0,
    "Pacific Ave": 0,
    "Pennsylvania Ave": 0
  } # List of Green Properties

cash = 2000

purchases_needed = 0
bank_houses = 0
bank_hotels = 0


# # #"main"
# Start program if you own all green properties
start = str(input("Do you own all green properties? (y/n): "))

if start.lower() == 'n':
    print("[You cannot purchase a hotel until you own\n         all the properties of a given color group.]")


# Program Runs
while start == 'y':

    set_variables()
    # # Check to make sure set_variables worked
    # for each in g_prop.values():
    #     print(each)
    # print(cash)
    # print(bank_houses)
    # print(bank_hotels)

    if g_prop["Pennsylvania Ave"] == 5:
        print(f"[You cannot purchase a hotel if the property already has one.]")
        start = 'n'
        break

    # Decision Tree for Each Property, 
    #  # (order of NC & PC Ave shouldn't matter, but PA Ave must be last.)
    for prop in g_prop.values():
        if prop >= 4:
            pass
        else:
            purchases_needed += (4-prop)
    print(f"You Need To Buy: {purchases_needed} houses.")

    # Check's if there is enough houses for purchase,
    # If there is, check if you can afford them & still have money for a Hotel
    if purchases_needed > bank_houses:
        print("[There are not enough houses available for purchase at this time.]")
        break
    else:
        if purchases_needed > 0:
            start = afford_buildings(purchases_needed, cash)
        else:
            pass
    # Check if able to continue
    if start == 'n':
        break

    # Check to see if you can swap Hotels or want to.
    # If you swap Hotels, the program Ends
    swap_check = swap_hotels()

    # You choose/cannot swap for a Hotel
    if swap_check == 'n':
        if bank_hotels < 1:
            print("[There are not enough hotels available for purchase at this time.]")
            start = 'n'
            break
        elif cash >= 200:
            print("The Hotel will cost $200.")
            print("     You purchase 1 Hotel.")
            print("     Put Put 1 hotel on Pennsylvania and return any houses to the bank.")
            start = 'n'
        elif cash < 200:
            print("You do not have sufficient funds to purchase a hotel at this time.")
            start = 'n'
    elif swap_check == 'y':
        start = 'n'



print("\nEnd of Program\n")