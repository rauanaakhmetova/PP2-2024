#Ex1
x = "Hello World"
print(len(x))
#Ex2
txt = "Hello World"
x = txt[0]
#Ex3
txt = "Hello World"
x = txt[2:5]
#Ex4
txt = "Hello World"
x = txt[2:5]
#Ex5
txt = "Hello World"
txt = txt.upper()
#Ex6
txt = "Hello World"
txt = txt.lower()
#Ex7
txt = "Hello World"
txt = txt.replace("H", "J")
#Ex8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#examples
#1Get the character at position 1 of a string
a = "Hello, World!"
print(a[1])
#2 Substring. Get the characters from position 2 to position 5 (not included)
b = "Hello, World!"
print(b[2:5])
#3 Remove whitespace from the beginning or at the end of a string
a = " Hello, World! "
print(a.strip())
#4 Return the length of a string
a = "Hello, World!"
print(len(a))
#5 Convert a string to lower case
a = "Hello, World!"
print(a.lower())
#6Convert a string to upper case
a = "Hello, World!"
print(a.upper())
#7 Replace a string with another string
a = "Hello, World!"
print(a.replace("H", "J"))
#8 Split a string into substrings
a = "Hello, World!"
b = a.split(",")
print(b)

