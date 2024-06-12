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

a = int(input("Enter a number: "))
if a % 2 == 0:
    print("Even")
else:
    print("Odd")
    