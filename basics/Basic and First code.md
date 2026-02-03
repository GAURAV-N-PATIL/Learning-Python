````md
# 🐍 First Python Code

```python
print("Hello, World!")
````

---

## 🔑 Reserved Words in Python (Keywords)

Python has some **reserved words** called **keywords**.

⚠️ You cannot use these keywords as:

* Variable names
* Function names
* Class names
* Any other identifiers

### ✅ List of Python Keywords

```
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

---

## ⚙️ Interpreter and Compiler

Python is a **high-level language**, but the CPU understands only **low-level machine language**.

So, Python code must be converted into low-level instructions.

This conversion is done by:

* **Interpreter**
* **Compiler**

---

## 🟢 Interpreter in Python

Python uses an **Interpreter**.

### How the Interpreter Works

* Converts code **line by line**
* Executes each line immediately
* Continues until the entire program finishes

This process is commonly done in:

* Terminal
* Command Prompt

---

## 🔵 Compiler (General Concept)

A **Compiler** works differently:

* Converts the **whole program at once**
* Then executes it

### File Extensions for Compiled Languages

Compiled languages usually use:

```
.c, .cpp, .java
```

Python files use:

```
.py
```

Python programs can be run using tools like:

* VS Code
* PyCharm
* Jupyter Notebook

---

# ❌ Errors Types in Python

Errors are common while programming.
Below are the most important error types in Python:

---

## 1. Syntax Error

Occurs when code is not written in proper format.

```python
print("Hello World")   # Correct Syntax
print("Hello World'    # Incorrect Syntax (missing closing quote)
```

---

## 2. Logical Error

Occurs when code is syntactically correct but produces incorrect results.

```python
a = "hello"
b = 10
c = a + b  # Logical Error: string + integer makes no sense
```

---

## 3. Runtime Error

Occurs during program execution.

```python
a = 10
b = 0
c = a / b  # Runtime Error: Division by zero is not allowed
```

---

## 4. Indentation Error

Occurs when code is not properly indented.

```python
if True:  # Correct indentation
    print("Hello World")

if True:  # Incorrect indentation
print("Hello World")
```

---

## 5. Type Error

Occurs when an operation is performed on incompatible data types.

```python
a = "hello"
b = 10
c = a + b  # Type Error: Cannot concatenate string and integer
```

---

## 6. Name Error

Occurs when a variable or function is not defined.

```python
print(x)  # Name Error: x is not defined
```

---

## 7. Value Error

Occurs when the correct type is given but the value is inappropriate.

```python
int("hello")  # Value Error: Cannot convert string to integer
```

---

## 8. Index Error

Occurs when trying to access an index out of range.

```python
my_list = [1, 2, 3]
print(my_list[5])  # Index Error: List index out of range
```

---

## 9. Key Error

Occurs when trying to access a missing key in a dictionary.

```python
my_dict = {"a": 1, "b": 2}
print(my_dict["c"])  # Key Error: 'c' not found
```

---

## 10. Attribute Error

Occurs when an object does not have the attribute being accessed.

```python
my_list = [1, 2, 3]
my_list.appendd(4)  # Attribute Error: 'list' has no attribute 'appendd'
```

---

## 11. Semantic Error

Occurs when code runs but does not do what the programmer intended.

```python
a = 5
b = 10
c = a - b  # Semantic Error: intended addition but subtracted instead
```

---

These are some common error types in Python.
Understanding them helps in debugging and writing better code.

---

# 🛠 Debugging in Python

Debugging is the process of:

✅ Finding errors
✅ Fixing errors

---

## Techniques for Debugging

1. Reading code carefully (**Code Review**)
2. Using print statements (to check variable values at each stage)
3. Using debugging tools (like `pdb`, IDE debuggers)
4. Reviewing error messages (to understand type and location)
5. Testing code in small parts (to isolate the problem)
6. Seeking help from others (forums, colleagues)
7. Reading documentation (to understand libraries and functions)
8. Practicing regularly (to improve skills and reduce errors)

---

By using these techniques, you can effectively debug Python code and improve your programming skills.

```
```
