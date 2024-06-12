# first = float(input("First: "))
# second = float(input("Second: "))
# total = first + second
# print("Total: ", str(total))

# course = 'Python for Biginners'
# print('for' in course)

# x = 10
# x*=3
# print (x)

# x = 3 != 2
# print (x)

# price = 25
# print(price > 10 or price < 20)

# temperature = 11
# if temperature > 30:
#     print("It's a hot day")
#     print("Drink water")
# elif temperature > 20:
#     print ("It's a nice day")
# elif temperature > 10:
#     print ("It's a cold day")
# else:
#     print("Temperature undetermined")
# print("Done")

# weight = int(input("Weight : "))
# conversion = input("K(g) or (L)bs: ")
# if conversion.lower() == 'g':
#     weight /= 0.45
#     print("{:.2f}".format(weight))
# else:
#     print("{:.2f}".format(weight))
# print("Conversion done.")

# weight = int(input("Weight: "))
# unit = input("(K)g or (L)bs: ")

# if unit.upper() == "K":
#     converted = weight * 2.20462  # converting kg to lbs
#     print("Weight in Lbs: " + str(converted))
# else:
#     converted = weight * 0.453592  # converting lbs to kg
#     print("Weight in Kgs: " + str(converted))

# i = 1
# while i <= 1_0: 
#     print(i * '*')
#     i = i+1

# name = ["James", "Lim"]
# name[0] = "Jon"
# print(name[0:2])

# nums = [0,1,2,3,4,5]
# nums.insert(6,6)
# print(len(nums))
# nums.remove(5)
# print(nums)
# print(5 in nums)
# print(len(nums))

# nums = [1,2,3,4,5]
# # for items in nums:
# #     print (items)
    
# i = 0
# while i < len(nums):
#     print(nums[i])
#     i = i + 1

# numbers = range(5,10, 4)
# for number in numbers:
#     print(number)

# numbers = (1,2,3)
# numbers.count(2)

# name = input("What is your name? ")
# length= len(name)
# print(length)
# newlength = str(length)
# print(type(length))
# print(type(newlength))

# a = 123.12
# newtype = int(a)
# print(newtype)

# years_input = input('Enter number of years: ')
# week_convert = (int)(years_input) * 52
# newYears_input = str(years_input)
# newWeek_input = str(week_convert)
# print ("There are " + newWeek_input + " weeks in " + newYears_input + " years")

# years_input = input('Enter number of years: ')
# week_convert = (int)(years_input) * 52
# print (f"There are {week_convert} weeks in {years_input} years.")

# print("Welcome to the Group Name Generator")
# color = input("What is favourite color? ")
# animal = input("What is favourite animal? ")
# print (f"You group name could be {color} {animal}")

# hours = input("Enter Hours: ")
# rate = input("Enter Rate: ")
# pay = int(hours) * float(rate)
# print(f"{pay:.2f}")

# celcius = input("Enter temperature in Celsius: ")
# fahrenheit = (int(celcius) * 9 / 5) + 32
# print(f"{int(fahrenheit)} Fahrenheit")

# print("Welcome to the Trip Cost Calculator!")
# hotel_days = input("How many days will you stay? ")
# hotel_cost = input("How much hotel cost per night? $")
# flight_cost = input("How much does flight cost? $")
# car_rental = input("If you need rental car please enter the price otherwise enter zero. $")
# other_expenses = input("Enter other possible expenses: $")
# total_cost = (float(hotel_days) * float(hotel_cost)) + float(flight_cost) + float(car_rental) + float(other_expenses)
# print(f"Total Cost: ${total_cost:.2f}")

# boolean = 2 > 1
# print(boolean)

# print ("Welcome")
# salary = int(input("What is your salary?"))
# if salary > 2000:
#     print("Nice")
# else:
#     print("Not nice")

# a = int(input("Enter a number: "))
# if a % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# salary = int(input("What is your salary? :"))
# if(salary > 2000):
#     print("More than 2000")
#     credit_score = int(input("What is your credit score?"))
#     if credit_score > 800:
#         print("Interest rate 10%")
#     elif credit_score > 750:
#         print("INterest rate 9%")
#     else:
#         print("Interest rate 5%")
# else:
#     print("Sorry, your are not eligible")


# height = float(input("Enter your height in m: "))
# weight =  float(input("Enter your weight in kg: "))
# bmi = round(float(weight / height **2),1)
# if bmi < 18.5:
#     print(f"{bmi} is Underweight")
# elif bmi > 18.5 and bmi < 25:
#     print(f"{bmi} is Normal")
# elif bmi > 25 and bmi < 30:
#     print(f"{bmi} is Overweight")
# elif bmi > 30 and bmi < 35:
#     print(f"{bmi} is Obese")
# else:
#     print(f"{bmi} is an Invalid input")

# Display the burger menu
# print("Burger List:")
# print("Mini Burger (M): $5")
# print("Normal Burger (N): $8")
# print("Large Burger (L): $10")
# print("Add Mushroom: For Mini and Normal = $1, for Large = $2")
# print("Extra Cheese: $1")

# # Getting user inputs
# size = input("What type of burger do you want? (M/N/L): ").strip().upper()
# add_mushroom = input("Add Mushroom? Yes (Y) or No (N): ").strip().upper()
# extra_cheese = input("Extra Cheese? Yes (Y) or No (N): ").strip().upper()

# # Initialize cost and validate burger size
# cost = 0
# if size == "M":
#     cost = 5
#     print("You chose Mini Burger.")
# elif size == "N":
#     cost = 8
#     print("You chose Normal Burger.")
# elif size == "L":
#     cost = 10
#     print("You chose Large Burger.")
# else:
#     print("Invalid burger size selected. Please choose M, N, or L.")
#     exit()  # Exit if the burger size is invalid

# # Adding cost for mushrooms
# if add_mushroom == "Y":
#     if size == "L":
#         cost += 2  # Large burger mushroom cost
#     else:
#         cost += 1  # Mini and Normal burger mushroom cost
#     print("Added Mushroom.")
# elif add_mushroom == "N":
#     print("No Mushroom added.")
# else:
#     print("Invalid input for mushrooms. Please choose Y or N.")
#     exit()  # Exit if the mushroom choice is invalid

# # Adding cost for extra cheese
# if extra_cheese == "Y":
#     cost += 1
#     print("Added Cheese.")
# elif extra_cheese == "N":
#     print("No Cheese added.")
# else:
#     print("Invalid input for cheese. Please choose Y or N.")
#     exit()  # Exit if the cheese choice is invalid

# # Display the total cost
# print(f"Your total cost is ${cost:.2f}.")


# Display the burger menu
print("Burger List:")
print("Mini Burger (M): $5")
print("Normal Burger (N): $8")
print("Large Burger (L): $10")
print("Add Mushroom: For Mini and Normal = $1, for Large = $2")
print("Extra Cheese: $1")

# Initialize cost variables
burger_cost = 0
total_cost = 0

# Getting user inputs
size = input("What type of burger do you want? (M/N/L): ").strip().upper()

# Validate burger size input
if size == "M":
    burger_cost = 5
    print("You chose Mini Burger.")
elif size == "N":
    burger_cost = 8
    print("You chose Normal Burger.")
elif size == "L":
    burger_cost = 10
    print("You chose Large Burger.")
else:
    print("Invalid burger size selected. Please choose M, N, or L.")
    exit()  # Exit if the burger size is invalid

# Use try-except to handle integer input for the number of burgers
try:
    num_burgers = int(input("How many burgers do you want to order? "))
    if num_burgers <= 0:
        raise ValueError("The number of burgers must be a positive integer.")
except ValueError as ve:
    print(f"Invalid input for the number of burgers: {ve}")
    exit()  # Exit if the input is not a valid positive integer

# Calculate the base cost based on the number of burgers
total_cost = burger_cost * num_burgers

# Getting additional options
add_mushroom = input("Add Mushroom? Yes (Y) or No (N): ").strip().upper()
extra_cheese = input("Extra Cheese? Yes (Y) or No (N): ").strip().upper()

# Adding cost for mushrooms
if add_mushroom == "Y":
    if size == "L":
        mushroom_cost = 2
    else:
        mushroom_cost = 1
    total_cost += mushroom_cost * num_burgers
    print(f"Added Mushroom. Additional cost: ${mushroom_cost * num_burgers:.2f}")
elif add_mushroom == "N":
    print("No Mushroom added.")
else:
    print("Invalid input for mushrooms. Please choose Y or N.")
    exit()  # Exit if the mushroom choice is invalid

# Adding cost for extra cheese
if extra_cheese == "Y":
    cheese_cost = 1
    total_cost += cheese_cost * num_burgers
    print(f"Added Cheese. Additional cost: ${cheese_cost * num_burgers:.2f}")
elif extra_cheese == "N":
    print("No Cheese added.")
else:
    print("Invalid input for cheese. Please choose Y or N.")
    exit()  # Exit if the cheese choice is invalid

# Display the total cost
print(f"Your total cost for {num_burgers} burger(s) is ${total_cost:.2f}.")

    
    



    