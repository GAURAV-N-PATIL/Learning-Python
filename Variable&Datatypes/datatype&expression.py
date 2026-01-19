#datatypes & expressions in Python
'''Data types in Python:
1.Numeric Data Types:
   a.Integer (int): Whole numbers, e.g., 10, -5, 0
   b.Float (float): Decimal numbers, e.g., 3.14, -0.001
   c.Complex (complex): Complex numbers, e.g., 2 + 3j
2.Sequence Data Types:
   a.String (str): Text data, e.g., "Hello, World!"
   b.List (list): Ordered collection of items, e.g., [1, 2, 3, "apple"]
   c.Tuple (tuple): Immutable ordered collection of items, e.g., (1, 2, 3)
    d.Range (range): Sequence of numbers, e.g., range(0, 10)
3.Mapping Data Type:
   a.Dictionary (dict): Key-value pairs, e.g., {"name": "John", "age": 30}
4.Set Data Types:
    a.Set (set): Unordered collection of unique items, e.g., {1, 2, 3}
    b.Frozenset (frozenset): Immutable version of a set, e.g., frozenset([1, 2, 3])
5.Boolean Data Type:
   a.Boolean (bool): Represents True or False values
6.Binary Data Types:
   a.Bytes (bytes): Immutable sequence of bytes, e.g., b"Hello"
    b.Bytearray (bytearray): Mutable sequence of bytes, e.g., bytearray(b"Hello")
    c.Memoryview (memoryview): View of binary data, e.g., memoryview(b"Hello")
7.bitwise Data Type:
    a.Bitwise (bit): Represents binary digits (0 and 1)
    bytes and Bytearray can also be used for bitwise operations.
'''

# Expressions in Python:
'''An expression is a combination of values, variables, operators, and function calls that can be evaluated
to produce a result.
Examples of expressions:
1.Arithmetic Expressions:
   a.Addition: 5 + 3
   b.Subtraction: 10 - 4
   c.Multiplication: 2 * 6
   d.Division: 8 / 2
   e.Floor Division: 7 // 3  ---> gives 2 i.e removes decimal part
   f.Modulus: 10 % 3  ---> gives 1
   g.Exponentiation: 2 ** 3  ---> gives 8
2.Comparison Expressions:
   a.Equality: 5 == 5
    b.Inequality: 5 != 3
    c.Greater than: 7 > 4
    d.Less than: 3 < 6
    e.Greater than or equal to: 5 >= 5
    f.Less than or equal to: 4 <= 7
3.Logical Expressions:
   a.And: True and False
    b.Or: True or False
    c.Not: not True
4.Assignment Expressions:
    a.Simple Assignment: x = 10
    b.Augmented Assignment: x += 5  i.e x = x + 5
5.Function Call Expressions:
   a.Function Call: len("Hello")
    b.Method Call: "Hello".upper()
6.Conditional Expressions:
    a.Ternary Operator: x if condition else y
7.Lambda Expressions:
   a.Lambda Function: lambda x: x + 1
8.Bitwise Expressions:
   a.Bitwise AND: a & b
    b.Bitwise OR: a | b
    c.Bitwise NOT: ~a
    d.Bitwise XOR: a ^ b
    e.Left Shift: a << 1
    f.Right Shift: a >> 1
These expressions can be combined and nested to create more complex expressions.
Operator Precedence in Python:
1.Parentheses: ()
2.Exponentiation: **
3.Unary Plus and Minus: +x, -x, ~x
4.Multiplication, Division, Floor Division, Modulus: *, /, //, %
5.Addition and Subtraction: +, -
6.Bitwise Shift Operators: <<, >>
7.Bitwise AND: &
8.Bitwise XOR: ^
9.Bitwise OR: |
10.Comparison Operators: ==, !=, >, <, >=, <=
11.Assignment Operators: =, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, >>=, <<=
12.Logical NOT: not
13.Logical AND: and
14.Logical OR: or
Operators with higher precedence are evaluated before operators with lower precedence.
'''
#precedency in python
'''
Operator Precedence in Python:
1.Parentheses: ()
2.Exponentiation: **
3.Unary Plus and Minus: +x, -x, ~x
4.Multiplication, Division, Floor Division, Modulus: *, /, //, %
5.Addition and Subtraction: +, -
6.Bitwise Shift Operators: <<, >>
7.Bitwise AND: &
8.Bitwise XOR: ^
9.Bitwise OR: |
10.Comparison Operators: ==, !=, >, <, >=, <=
11.Assignment Operators: =, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, >>=, <<=
12.Logical NOT: not
13.Logical AND: and
14.Logical OR: or
Operators with higher precedence are evaluated before operators with lower precedence.
'''
#statement in python
'''A statement is a complete line of code that performs a specific action.
Examples of statements:
1.Assignment Statement:
   x = 10
2.Expression Statement:
    print(x + 5)
3.Conditional Statement:
   if x > 5:
         print("x is greater than 5")
4.Loop Statement:
   for i in range(5):
        print(i)
5.Function Definition Statement:
   def greet(name):
        print("Hello, " + name)
6.Class Definition Statement:
   class Person:
        def __init__(self, name):
            self.name = name
7.Import Statement:
   import math
8.Return Statement:
   def add(a, b):
        return a + b
9.Break Statement:
   for i in range(10):
        if i == 5:
            break
10.Continue Statement:
    for i in range(10):
        if i % 2 == 0:
            continue
        print(i)
11.Pass Statement:
    def placeholder():
        pass
'''