#Ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#Ex2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#Ex3
for x in range(6):
  print(x)
#Ex4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#Examples
#The for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
#Loop through a string
for x in "banana":
  print(x) 
#Using the break statement in a for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break
#Using the continue statement in a for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 
#Using the range() function in a for loop
for x in range(6):
  print(x) 
#Else in for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#Nested for loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)