print("HELLO, WORLD")
# to take input from user
name = input("Name: " )
print(f"Hello, {name}") # the same of print("hello, "+ name)
#   conditions
n  = int(input("Number: "))
if n > 0 :
    print("number is positive")
elif n < 0 :
    print("number is negative")
else:
    print("number is zero")

#  SEQUENCES 
names = ["Harry", "Ron","Hermione"] #list 
print(names[0])
 
coordinatex = 10.0
coordinatey = 20.0

coordinate =(10.0 , 20.0) # tuple

#  define a  list of names
names = ["Harry", "Ron","Hermione", "Ginny"]
print (names)

names.append("Draco")#to add a value to the end of the list
names.sort()# to sort the valuses of the list in asec order


#  creatre an empty set
s = set()
# add elements to the set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
# if we add a value is already exists in the set it will not be added to the set 
# becasue the set is only have unique values no repettions


#  to remove elements form the set
s.remove(2)
print(s)
print(f" the set has {len(s)} elemensts.")


# loops
for i in [0,1,2,3,4,5]:
    print(i)
# the same 
for i in range(6):
    print(i)


names = ["Harry", "Ron","Hermione"] 
for name in names:
    print(name)

name= "Harry"
for char in name:
    print(char)

# dictionary with keys and values
houses = {"Harry":"Gryffindor", "Draco":"Slytherin"}
houses["Hermione"]= "Gryffindor"
print(houses["Harry"])



# functions 
from functions import square
for i in range(10): #from 0 to 9
    print(f"The square of {i} is: {square(i)}")
# the same as
# import funtcions
# for i in range(10): 
#     print(f"The square of {i} is: {functions.square(i)}")


