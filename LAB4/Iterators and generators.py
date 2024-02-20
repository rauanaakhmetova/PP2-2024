#1Create a generator that generates the squares of numbers up to some number N.
def squares(N):
    for i in range(1, N+1):
        yield i*i
N = int(input())
squares = squares(N)

print(N)
for square in squares:
    print(square)

#2Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_nums(n):
        for i in range(n+1):
            if i % 2 == 0:
                yield i

n = int(input())
even_numbers = even_nums(n)

for num in even_numbers:
    print(num, end="," if num != n and num != n-1 else "")

#3Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divisible_nums(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
div_nums = divisible_nums(n)
for num in div_nums:
    print(num, end="," if num != n and num != n-1 else "")

#4Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    for n in range (a, b+1):
        yield n*n
a = int(input())
b = int(input())

for square in squares(a, b):
    print(square)


#5Implement a generator that returns all numbers from (n) down to 0.
def reverse(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input())
nums_decreasing = reverse(n)
for num in reverse(n):
    print(num)