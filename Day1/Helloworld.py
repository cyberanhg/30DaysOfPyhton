import math

"""Exercise: Level 1
1.Check the python version you are using
2. Open the python interactive shell and do the following operations. The operands are 3 and 4 """

# python --version 

print("------------------------------------------------------------------------------")
print("Python 3.9.2")
print("------------------------------------------------------------------------------")
print("Addition: ", 3 + 4)  #addition(+)
print("Subtration: ", 3 - 4)  #subtration(-)
print("Multiplication: ", 3 * 4)  #multiplication(*)
print("Modulus: ", 3 % 4)  #modulus(%)
print("Exponential: ", 3 ** 4) #exponential(**)
print("Floor division: ", 3 // 4) #floor division operator(//)


"""Write strings on the python interactive shell. The strings are the following:
Your name
Your family name
Your country
I am enjoying 30 days of python"""

print("------------------------------------------------------------------------------")

name = 'Angie'
family = 'Espinoza'
country = 'El Salvador'
mensaje = 'I am enjoying 30 days of python :D!'

print("Name: ", name)
print("Family name: ", family)
print("Conuntry: ", country)
print(mensaje)

print("------------------------------------------------------------------------------")
"""4. Check the data types of the following data:
10
9.8
3.14
4 - 4j
['Asabeneh', 'Python', 'Finland']
Your name
Your family name
Your country """

print("int: ", 10)
print("float: ", 9.8)
print("float: ", 3.14)
print("complex: " , 4-4j)

list(['Asabeneh', 'Python', 'Finland'])
print("Tuple: " , name, family, country)

print("------------------------------------------------------------------------------")
""" Exercise: Level 2
Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use print() when you are working on a python file. Navigate to the directory where you have saved your file, and run it."""
#Completed
""" Exercise: Level 3
    1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
    2. Find an Euclidian distance between (2, 3) and (10, 8)"""

#1
Nentero = 10
Ndecimal = 3.14
Ncomplex = 9+3j
mensaje = str("Hello world:)!")
Vbool = True

Vlista = ["Queso", "Leche", "Huevos"]
Vturple = ("Dia ", 1, 2021, "Dinero", 23.08)
Vset = ([48, "Hola!", 2.20])
Vdic = {"numero": 10, "clave": "H1234"}

print("Integer: ", Nentero)
print("Float: " , Ndecimal)
print("Complex: ", Ncomplex)
print("String: " , mensaje)
print("Bool: " , Vbool)
print("List: ", Vlista)
print("Turple: ", Vturple)
print("Set: ", Vset)
print("Dictionary: ", Vdic)

#2             
puntox1 = float(2)
puntox2 = float(3)
puntoy1 = float(10)
puntoy2 = float(8)
distancia = float()

distancia = ((puntox2 - puntox1)**2) + ((puntoy2 - puntoy1)**2)
print("La distancia es de: ", math.sqrt(distancia))

print("------------------------------------------------------------------------------")

