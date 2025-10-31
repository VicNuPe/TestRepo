"""nam = [3, 5, 6, 9, 2]


nam.append(7)

print(nam[4])
print(nam[5])

nam.remove(3)
print(nam[3])


nam.sort()
print(nam)

print(len(nam))

"""

"""
num = []

count = 0
while count <= 4:
    val = int(input("Type a number:\n"))
    num.append(val)
    count += 1

print(num)
num.pop()
num.append(23)
num.sort()
print(num)
"""
'''
my_tuple = (10, 20, 30, 40, 60)
print(my_tuple)
print(len(my_tuple))


my_tuple = ("apple", "banana", "cherry")
print("banana" in my_tuple)

print(my_tuple + ("mango",))
print(my_tuple)


my_dict = {"name": "Victor", "age": 24, "city": "São Paulo", "student": True}
print(my_dict)
print(my_dict.keys())
my_dict.update({"Country": "Brasil", "age": 32})
print(my_dict)

new_my_dict = my_dict.copy()
new_my_dict.clear()
print(new_my_dict)'''

vdict = {"name": "Victor Nunes Pedreira", "age": 24, "grade": 9.5}
print(vdict)
vdict.update({"city": "São Paulo", "grade": 10})
print(vdict)
new_vdict = vdict.copy()
print(new_vdict)
new_vdict.clear()
print(new_vdict)

fruits = ("apple","banana","pear")
print(fruits)
numbers = (1,2,3,4,5)
print(numbers[0])
print(numbers[4])
print(len(numbers))

colors = ("red","green", "blue","yellow")
print(colors[2])

