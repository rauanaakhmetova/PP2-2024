#Ex1A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams
def ounces_to_grams(grams):
    ounces = 28.3495231 * grams
    return ounces
grams_we_need = float(input())
ounces_we_need = ounces_to_grams(grams_we_need)
print(ounces_we_need)

#Ex2Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)
def f_to_c(farenheit):
    cetnrigrade = (5/9)*(farenheit-32)
    return cetnrigrade
farenheit_we_got = float(input())
calculated_centrigrade = f_to_c(farenheit_we_got)
print(calculated_centrigrade)

#Ex3Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
def  solve(numheads, numlegs):
    rab = 0
    chik = 0
    rab = (numlegs-2*numheads)/2
    chik = numheads-rab
    if rab >= 0 and chik >=0 and rab.is_integer()  and chik.is_integer():
        return int(rab), int(chik)
    else:
        return 0
numheads = int(input())
numlegs = int(input())
numchik, numrab = solve(numheads, numlegs)
print(numchik)
print(numrab)

#Ex4***
"""
def number_list():
    numbers = input().split()
    numbers = [int(num) for num in numbers]
    return numbers

def prime_nums(nums):
    if nums <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if nums % i == 0:
            return False
    return True
def filter_primes(numbs):
    pr_nums =[nums for nums in numbs if prime_nums(nums)]
    return pr_nums
    pr_nums = filter_primes(numbs)
    print(pr_nums)
    """

#Ex5Write a function that accepts string from user and print all permutations of that string.
from itertools import permutations

def print_permutations(string):
    perms = permutations(string)
    for perm in perms:
        print(''.join(perm))
user_input = input()
print_permutations(user_input)

#6ExWrite a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We
def reverse(words):
    sent = words.split()
    reverse = sent[::-1]
    reverse_sent = ' '.join(reverse)
    return reverse_sent
sentence = input()
reverse_sent = reverse(sentence)
print(reverse_sent)

#Ex7Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    for i in range (len(nums)-1):
        if nums[i] == 3 and nums [i +1] == 3:
            return True
    return False

def input_has_33():
    numbers = input()
    numbers = [int(num) for num in numbers.split()]
    return numbers

input_nums = input_has_33()
print(has_33(input_nums))


#Ex8Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    for i in range (len(nums)-1):
        if nums[i] == 0 and nums [i +1] == 0 and nums [i +2] == 7:
            return True
    return False

def input_spygame():
    numbers = input()
    numbers = [int(num) for num in numbers.split()]
    return numbers

input_nums = input_spygame()
print(spy_game(input_nums))

#Ex9Write a function that computes the volume of a sphere given its radius.
import math
def calculate_volume(r):
    volume = (4/3)*(r*r*r)*math.pi
    return volume
r = float(input())
volume = calculate_volume(r)
print(volume)

#Ex10Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.
