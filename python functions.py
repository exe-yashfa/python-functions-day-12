def my_function():
    print("Hello from a function")
my_function()
my_function()
my_function()

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

def get_greeting():
    return "Hello from a function"
message = get_greeting()
print(message)

def get_greeting():
 return "Hello from a function"
print(get_greeting())

def my_function(fname):
    print(fname + "Refsnes")
my_function("Email")
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

def my_function(name = "friend"):
    print("Hello",name)
my_function("Email")
my_function("Tobias")
my_function()
my_function("Linus")

def my_function(country = "Norway"):
   print("I am from", country)
my_function("Sweden")
my_functuion("India")
my_function()
my_function("Brazil")

def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

def my_function(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + 's name is', name)
my_function(animal = "dog", name = "Buddy")

def my_function(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

def my_function(x, y):
    return x + y
result = my_function(5, 3)
print(result)

def my_function():
    return["apple", "banana", "cherrry"]
print(fruit[0])
print(fruit[1])
print(fruit[2])

def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

def my_function(name, /):
    print("Hello", name)

my_function("Emil")



def my_function(name):
  print("Hello", name)

my_function(name = "Emil")
def my_function(a, b, /, *, c, d):
    return a + b + c + d
result = my_function(5, 10, c = 15, d = 20)
print(result)

def my_function(*kids):
    print("The youngest child is " +kids[2])
my_function("Emil", "Tobias", "Linus")


def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")





























































