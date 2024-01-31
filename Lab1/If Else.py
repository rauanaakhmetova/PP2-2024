#Ex1
a = 50
b = 10
if a > b:
  print("Hello World")
#Ex2
a = 50
b = 10
if a != b:
  print("Hello World")
#Ex3
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")
#Ex4
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")
#Ex7
  if 5 > 2:
    print("YES")
#Ex8
a = 2
b = 5
print("YES") if a == b else print("NO")
#Ex9
a = 2
b = 50
c = 2
if a == c or b == c:
  print("YES")


#Examples
#The if statement
a = 33
b = 200

if b > a:
  print("b is greater than a")
#The elif statement
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#The else statement
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#Short hand if
a = 200
b = 33

if a > b: print("a is greater than b")
#Short hand if ... else
a = 2
b = 330

print("A") if a > b else print("B")
#The and keyword
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#The or keyword
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
