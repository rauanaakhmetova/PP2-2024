#Ex 1
class strings():
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())

name = strings()
name.getString()
name.printString()
        
#Ex2
class Shape:
    def __init__(self):
        self.a = 0
    def area(self):
        print(self.a)

class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.length = length
        self.a = self.length**2

x1 = Shape()
x2 = Square(4)
x1.area()
x2.area()

#Ex3     
import ex02

class Rectangle(ex02.Shape):
    def __init__(self, l, w):
        ex02.Shape.__init__(self)
        self.l = l
        self.w = w
    def area(self):
        return self.l*self.w

r = Rectangle(4, 5)
print(r.area())

#Ex4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f'(x, y) = {self.x, self.y}')
    
    def move(self, x1, y1):
        self.x += x1
        self.y += y1
    
    def dist(self, x1, y1):
        return ( (self.x - x1)**2 + (self.y - y1)**2)**(1/2)

p = Point(1, 2)

p.show()

p.move(+1, -5)
p.show()

print(f'distance = {p.dist(0, 0)}')

#Ex5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, money):
        self.balance += money
    
    def withdraw(self, money):
        if self.balance - money >= 0: self.balance -= money
        else: print(f'doesn\'t enough, you have only - {self.balance}tg')
    
    def __str__(self):
        return f'name: {self.owner} \nbalance: {self.balance}'

me = Account('Daryn', 5000)
print(me)

me.deposit(400)
print(me)

me.withdraw(3000)
print(me)

me.withdraw(7000)
print(me)

#Ex6
def pr(n):
    if n<2: return False
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True

l = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

nums = list(filter(lambda x:pr(x), l))
print(nums)
    

