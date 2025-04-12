import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))

except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)


try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)# that means exit the programm because something went worng
print(f" {x} / {y} = {result}")
# it will be an error called ZeroDivisionError happens when y=0
# it will be an error called ValueError if the uset input a string value