#Ex1
def my_function():
    print("Hello from a function")

#Ex2
def my_function():
  print("Hello from a function")
my_function()

#ex3
def my_function(fname, lname):
  print(fname)

#Ex4
def my_function(x):
   return x+5

#ex5
def my_function(*kids):
  print("The youngest child is " + kids[2])

#Ex6
def my_function(**kids):
    print("The youngest child is " + kids[2])

#Examples
#1Create and call a function
def my_function():
  print("Hello from a function")

my_function()
#2 Function parameters
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#3Default parametr values 
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#4Let a function return a value
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#5Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

