"""
color = input("Type a color:")

match color:
    case "red":
        print("Stop!")
    case "green":
        print("Go!")
    case "yellow":
        print("Ready!")
    case _:
        print("Invalid color!")
"""

"""
num = int(input("Type a number:"))

message = "Zero" if num == 0 else "Non-zero"

print(message)
"""
"""
value = int(input("Type a number:"))

for i in range(1, 11):
    print(f"" + str(value) + " x " + str(i) + " = " + str(value * i))
"""

"""
for i in range(1, 11):
    print(f"The square root of {i} is {i * i} ")
"""
"""
password = "vitinho123"

entry = ""

while password != entry:
    entry = input("Type the code:\n")
print("Access Granted!")
"""

"""for i in range(1,50):
    if i == 3:
        continue
    if i == 26:
        break
    print(i)
"""

"""def addition(a, b):
    sum = a + b
    return sum

result = addition(10, 26)

print(result)
"""

"""def average(a,b,c):
    res = (a + b + c) / 3
    return res

print(average(25,45,45))
"""

'''
def square(a):
    res = a * a
    return res


print(square(5))
'''

'''def cube(a):
    res = a ** 3
    return res


print(cube(5))]
'''
'''
def isEven(a):
    if a % 2 == 0:
        return True
    else:
        return False
6
print(isEven())
'''

'''def isBigger(a,b):
    if a > b:
        return True
    else:
        return False

print(isBigger(19,9))
'''

'''x = 10

def demo():
    x = 5
    print(f'Local variable {x}')
    
demo()
print(f'Global variable {x}')
'''
b = 50

def add(a):
    num = a + b
    return num

def minus(a):
    num = a - b
    return num

'''def multiply(a):
    num = a * b
    return num

def divide(a):
    num = a / b
    return num


print(add(50))
print(minus(50))
print(multiply(50))
print(divide(50))'''


