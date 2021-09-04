import math

#Exercises - Day 2
"""Exercises: Level 1
1.  Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
2.  Write a python comment saying 'Day 2: 30 Days of python programming'/
3.  Declare a first name variable and assign a value to it /
4.  Declare a last name variable and assign a value to it /
5.  Declare a full name variable and assign a value to it/
6.  Declare a country variable and assign a value to it/
7.  Declare a city variable and assign a value to it/
8.  Declare an age variable and assign a value to it/
9.  Declare a year variable and assign a value to it/
10. Declare a variable is_married and assign a value to it/
11. Declare a variable is_true and assign a value to it/
12. Declare a variable is_light_on and assign a value to it
13. Declare multiple variable on one line """

# Day 2: 30 Days of python programming!

first_name = 'Angie'
last_name = 'Espinoza'
full_name = 'Angie Espinoza'
country = 'El Salvador'
city = 'San Salvador'
age = 18
year = 2021
is_married = False
is_true = True
is_light_on = False
hobbies = ({'Draw', 'take pictures', 'read'})

#Exercises: Level 2
#1 Check the data type of all your variables using type() built-in function
print("Dato tipo: ", type(first_name) , "Valor de la varible: ", first_name)
print("Dato tipo: ", type(last_name), "valor de la variable: ", last_name)
print("Dato tipo: ",type(country), "Valor de la variable: ", country)
print("Dato tipo: ",type(city), "Valor de la variable: ", city)
print("Dato tipo: ",type(age), "Valor de la variable: ", age)
print("Dato tipo: ",type(year), "Valor de la variable: ", year)
print("Dato tipo: ",type(is_married), "Valor de la variable: ", is_married)
print("Dato tipo: ",type(is_true), "Valor de la variable: ", is_true)
print("Dato tipo: ",type(is_light_on), "Valor de la variable: ", is_light_on)
print("Dato tipo: ",type(hobbies), "Valor de la variable: ", hobbies)

print("---------------------------------------------------------------------")
#2. Using the len() built-in function, find the length of your first name
print("Cantidad de valores de ", first_name ,": ",len(first_name))

print("---------------------------------------------------------------------")
#3. Compare the length of your first name and your last name
print("Cantidad de valores de mi nombre ", first_name ,": ", len(first_name) , ", Apellido: ", last_name , " Cantidad: ", len(last_name))
print("Nombre completo: ", full_name , "cantidad de valores: " , len(full_name))

print("---------------------------------------------------------------------")
"""4. Declare 5 as num_one and 4 as num_two
    -Add num_one and num_two and assign the value to a variable total
    -Subtract num_two from num_one and assign the value to a variable diff
    -Multiply num_two and num_one and assign the value to a variable product
    -Divide num_one by num_two and assign the value to a variable division
    -Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
    -Calculate num_one to the power of num_two and assign the value to a variable exp
    -Find floor division of num_one by num_two and assign the value to a variable floor_division""" 

num_one = 5
num_two = 4
Op_suma = num_one + num_two
Op_diff = num_two - num_one
Op_multiply = num_two * num_one
Op_div = num_one / num_two
Op_modulus = num_one % num_two
Op_power = num_one ** num_two
Op_floor = num_one // num_two

""" 5. The radius of a circle is 30 meters.
    -Calculate the area of a circle and assign the value to a variable name of area_of_circle
    -Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
    -Take radius as user input and calculate the area. """

#Area of a circle

radius = float(input("Ingresar radio del circulo: "))
area_of_circle   = float(math.pi * (radius**2))
print("Área del circulo: ", area_of_circle)
area_of_circle

print("---------------------------------------------------------------------")
#Circumference of circle

circum_of_circle = 2 * math.pi * radius
print("Circunferencia de un circulo: ", circum_of_circle) 
#radius 
area_of_circle 

# 6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names"""
print("---------------------------------------------------------------------")
name = input("Name: ")
last_name = input("Last name: ")
country = input("Country: ")
age = input("Age: ")

