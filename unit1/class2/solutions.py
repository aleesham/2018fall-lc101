#############################
### Chapter 4: Exercise 6 ###
#############################

# import modules
import turtle 

# prompt the user for 4 things: 
# number of sides
num_of_sides = int(input("Number of sides:"))

# length of side
len_of_sides = int(input("Length of sides:"))

# color (of the turtle)
border_color = input("Color of border:")

# fill color
fill_color = input("Color of polygon:")

# draw a regular polygon:

# set up the window
wn = turtle.Screen()

# set up the turtle: configure colors as well
t = turtle.Turtle()
t.color(border_color)
t.fillcolor(fill_color)
t.speed(5)

# A regular polygon is a shape with equal sides and equal angles
angle_to_turn = 360 / num_of_sides

# we already defined len_of_sides above

t.begin_fill()

for turn_num in range(num_of_sides):
    t.forward(len_of_sides)
    t.left(angle_to_turn)

t.end_fill()



##############################
### Chapter 4: Exercise 10 ###
##############################

# import modules
import turtle 

# set up screen
wn = turtle.Screen()
wn.bgcolor("lightgreen")

# set up turtle
alex = turtle.Turtle()
alex.color("blue")
alex.shape("turtle")
alex.speed(0)

alex.penup()

# configure if you want based on number of ticks
# in our case of a clock, there should be 12
number_of_ticks = 12
degrees_to_turn = 360/number_of_ticks

for tick in range(number_of_ticks):
    alex.forward(100)
    alex.pendown()
    alex.forward(20)
    alex.penup()
    alex.forward(20)
    alex.stamp()
    alex.forward(-140)
    alex.left(degrees_to_turn)


##############################
### Chapter 4: Exercise 12 ###
##############################

import turtle
alex = turtle.Turtle()
print(type(alex))
