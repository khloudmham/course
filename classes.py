class Point():
    def __init__(self, input1, input2):
        self.x = input1 
        self.y = input2

p = Point(2,8)
print(p.x)
print(p.y)


class Flight():
    def  __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self,name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)




flight = Flight(3)
people = ["Harry","Ron","Hermoine","Ginny"]
for person in people :
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f" NO available seats for {person}")


#  decorators are functions that take a functiuon as input 
# def announce(f):
#     def wrapper():




# lambda      

groupofpeople =[
    {"name": "Harry", "house":"Gryffindor"},
    {"name": "Cho", "house":"Ravenclaw"},
    {"name": "Draco", "house":"Slytherin"}
]


groupofpeople.sort()# will make a type error 

# def f(person):
#     return person["name" ]

# people.sort(key=f) the same as next line
people.sort(key=lambda person: person["name"])
# lambda 