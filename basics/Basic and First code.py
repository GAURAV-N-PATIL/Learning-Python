#First code
print("Hello, World!")


'''Reserved Words in Python or Keywords in Python
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
You cannot use these keywords as variable names, function names, or any other identifiers.
'''
"""Python is high-level language but to order CPU which is low-level language we need to convert
high-level language to low-level language. This process is done by Interpreter or Compiler."""
#In Python, we use Interpreter.
"""Interpreter is done line by line. It means it converts one line of code to low-level language
and then executes it. After that, it converts the next line of code to low-level language and executes it.
This process continues until all lines of code are executed. it is done in terminal or command prompt."""
#Compiler converts the whole code to low-level language at once and then executes it.
"""for compiler we need to save complete code in a file with .c, .cpp, .java extension etc.(here .py
is used for python files) and then we need to run that file in terminal or command prompt.
compiler like vs code, pycharm, jupiter etc are used for this purpose."""

'''#Errors types in Python:
1.Syntax Error: It occurs when the code is not written in proper format.
Example: print("Hello World") #Correct Syntax
         print("Hello World' #Incorrect Syntax - Missing closing quotation mark
2.Logical Error: It occurs when the code is syntactically correct but produces incorrect results.
Example: a = 'hello'
         b = 10
         c = a + b  #Logical Error: Should be string + integer makes no sense.
3.Runtime Error: It occurs during the execution of the program.
Example: a = 10
         b = 0
         c = a / b  #Runtime Error: Division by zero is not allowed.
4.Indentation Error: It occurs when the code is not properly indented.
Example: if True:  #Correct Indentation
        .....print("Hello World")
        if True:  #Incorrect Indentation
        ...print("Hello World")
5.Type Error: It occurs when an operation is performed on incompatible data types.
Example: a = 'hello'
         b = 10
         c = a + b  #Type Error: Cannot concatenate string and integer.
6.Name Error: It occurs when a variable or function is not defined.
Example: print(x)  #Name Error: 'x' is not defined.
7.Value Error: It occurs when a function receives an argument of the correct type but an inappropriate value.
Example: int('hello')  #Value Error: Cannot convert string 'hello' to integer.
8.Index Error: It occurs when trying to access an index that is out of range for a list or string.
Example: my_list = [1, 2, 3]
         print(my_list[5])  #Index Error: List index out of range.
9.Key Error: It occurs when trying to access a key that does not exist in a dictionary
Example: my_dict = {'a': 1, 'b': 2}
         print(my_dict['c'])  #Key Error: 'c' not found in dictionary.
10.Attribute Error: It occurs when trying to access an attribute that does not exist for an object.
Example: my_list = [1, 2, 3]
         my_list.appendd(4)  #Attribute Error: 'list' object has no attribute 'appendd'.
11.semantic Error: It occurs when the code is syntactically correct but does not do what the programmer intended.
Example: a = 5
        b = 10
        c = a - b  #Semantic Error: Programmer intended to add but subtracted instead.
These are some common error types in Python. Understanding these errors can help in debugging and writing better code.
'''
#debugging: It is the process of finding and fixing errors in the code.
"""Techniques for debugging:
1.Reading code carefully (code review)
2.Using print statements (to check variable values at every stages)
3.Using debugging tools (like pdb, IDE debuggers)
4.Reviewing error messages  (to understand the type and location of error)
5.Testing code in small parts (to isolate the problem)
6.Seeking help from others  (like online forums, colleagues)
7.Reading documentation   (to understand how functions and libraries work)
8.Practicing regularly   (to improve coding skills and reduce errors)
By using these techniques, you can effectively debug your Python code and improve your programming skills.
"""
