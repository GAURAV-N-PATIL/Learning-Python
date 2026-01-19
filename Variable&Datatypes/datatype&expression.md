# 📘 Datatypes, Expressions & Statements in Python

---

## 🧩 Data Types in Python

### 1. Numeric Data Types
- **Integer (`int`)**  
  ```python
  10, -5, 0
  ```

- **Float (`float`)**  
  ```python
  3.14, -0.001
  ```

- **Complex (`complex`)**  
  ```python
  2 + 3j
  ```

---

### 2. Sequence Data Types
- **String (`str`)**  
  ```python
  "Hello, World!"
  ```

- **List (`list`)**  
  ```python
  [1, 2, 3, "apple"]
  ```

- **Tuple (`tuple`)**  
  ```python
  (1, 2, 3)
  ```

- **Range (`range`)**  
  ```python
  range(0, 10)
  ```

---

### 3. Mapping Data Type
- **Dictionary (`dict`)**  
  ```python
  {"name": "John", "age": 30}
  ```

---

### 4. Set Data Types
- **Set (`set`)**  
  ```python
  {1, 2, 3}
  ```

- **Frozenset (`frozenset`)**  
  ```python
  frozenset([1, 2, 3])
  ```

---

### 5. Boolean Data Type
```python
True, False
```

---

### 6. Binary Data Types
- **Bytes (`bytes`)**  
  ```python
  b"Hello"
  ```

- **Bytearray (`bytearray`)**  
  ```python
  bytearray(b"Hello")
  ```

- **Memoryview (`memoryview`)**  
  ```python
  memoryview(b"Hello")
  ```

---

### 7. Bitwise Data Type
- Represents binary digits (0 and 1)  
- `bytes` and `bytearray` support bitwise operations

---

## 🧮 Expressions in Python

### 1. Arithmetic Expressions
```python
5 + 3
10 - 4
2 * 6
8 / 2
7 // 3
10 % 3
2 ** 3
```

---

### 2. Comparison Expressions
```python
5 == 5
5 != 3
7 > 4
3 < 6
5 >= 5
4 <= 7
```

---

### 3. Logical Expressions
```python
True and False
True or False
not True
```

---

### 4. Assignment Expressions
```python
x = 10
x += 5
```

---

### 5. Function Call Expressions
```python
len("Hello")
"Hello".upper()
```

---

### 6. Conditional Expression
```python
x if condition else y
```

---

### 7. Lambda Expression
```python
lambda x: x + 1
```

---

### 8. Bitwise Expressions
```python
a & b
a | b
~a
a ^ b
a << 1
a >> 1
```

---

## ⚙️ Operator Precedence in Python

1. `()`
2. `**`
3. `+x`, `-x`, `~x`
4. `* / // %`
5. `+ -`
6. `<< >>`
7. `&`
8. `^`
9. `|`
10. `== != > < >= <=`
11. `= += -= *= /= //= %= **= &= |= ^= >>= <<=`
12. `not`
13. `and`
14. `or`

---

## 🧾 Statements in Python

### Assignment Statement
```python
x = 10
```

### Expression Statement
```python
print(x + 5)
```

### Conditional Statement
```python
if x > 5:
    print("x is greater than 5")
```

### Loop Statement
```python
for i in range(5):
    print(i)
