#python variables
'''A variable is a container that holds data or value.
In Python, we do not need to declare a variable before using it.
We can create a variable and assign a value to it in a single line.
We can use any name for a variable except reserved words or keywords in Python.
Variable names can contain letters, numbers, and underscores (_).
Variable names cannot start with a number.
Variable names are case-sensitive. (name, Name and NAME are three different variables)
We can assign any data type to a variable.
We can change the value of a variable at any time.'''
#Example:
x = 10          #Integer variable
y = 3.14        #Float variable
name = "John"   #String variable
is_valid = True #Boolean variable
#We can print the value of a variable using the print() function.
print(x)
print(y)
print(name)
print(is_valid)
#We can change the value of a variable by assigning a new value to it.
x = 20
y = 6.28
name = "Doe"
is_valid = False
print(x)
print(y)
print(name)
print(is_valid)
#We can also assign the value of one variable to another variable.
a = x
b = y
c = name
d = is_valid    
print(a)
print(b)
print(c)
print(d)
#We can assign multiple variables in a single line.
p, q, r, s = 1, 2.5, "Hello", True
print(p)
print(q)
print(r)
print(s)
#We can swap the values of two variables without using a temporary variable.
m = 5
n = 10
m, n = n, m
print(m)
print(n)