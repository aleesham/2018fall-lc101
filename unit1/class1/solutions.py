#############################
### Chapter 2: Exercise 3 ###
#############################

# Prompt the user for the current time
current_time = input("What is the current time")
current_time = int(current_time)

# Prompt the user for waiting time
waiting_time = input("What is the waiting time")
waiting_time = int(waiting_time) 

# Calculate the new time 
new_time = (current_time + waiting_time) % 24

# Output what the hour will be 
print(new_time)



#############################
### Chapter 2: Exercise 7 ###
#############################

# Set pi as a constant
pi = 3.14 

# Prompt the user for radius
radius = float(input("What is your radius?"))

# Calculate area
area = pi * radius * radius

# Output area
print(area)



#############################
### Chapter 2: Exercise 9 ###
#############################

# Prompt the user to enter the number of miles driven 
miles_driven = float(input("How many miles have you drives?"))

# Prompt the user to enter the number of gallons used
gallons_used = float(input("How many gallons did you use?"))

# calculate miles / gallon
mpg = miles_driven / gallons_used

# Output: Your car gets ???? miles per gallon.
print("Your car gets " + str(mpg) + " miles per gallon.")



##############################
### Chapter 2: Exercise 11 ###
##############################

# Prompt the user for temperature in Fahrenheit
fahrenheit = float(input("What is the temperature in Fahrenheit?"))

# Google the Fahrenheit to Celsius formula
# Calculate Celsius
celsius = (5/9) * (fahrenheit - 32)

# Output: Your car gets ???? miles per gallon.
print(str(fahrenheit) + " degrees Fahrenheit is " + str(celsius) + " degrees Celsius." )



#############################
### Chapter 3: Exercise 2 ###
#############################

spins = input("How many times did you spin? (Enter a negative number for counter-clockwise spins) ")

degrees = float(spins) * 360 % 360

print("You are facing", degrees, "degrees relative to north")



#############################
### Chapter 3: Exercise 3 ###
#############################
current_temp_string = input("Enter a temperature in degrees Fahrenheit: ")
current_temp = int(current_temp_string)

current_temp_celsius = (current_temp - 32) * (5/9)
print("The temperature in Celsius is:", current_temp_celsius)



#############################
### Chapter 3: Exercise 4 ###
#############################
num_touchdowns = input("How many touchdowns were scored? ")
num_field_goals = input("How many field goals were scored? ")

total_score = 10 * int(num_touchdowns) + 5 * int(num_field_goals)

print("The team has", total_score, "points")