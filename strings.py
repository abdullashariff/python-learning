# Python String Built-in Functions and Methods

## Definition
# String functions are built-in methods that allow you to manipulate and work with string data in Python.

## 1. Basic String Functions

### Examples:
# ```python
text = "  Hello World!  "
name = "john doe"
numbers = "123"

# Basic built-in functions
print("len(text):", len(text))                    # Length of string
print("str(123):", str(123))                      # Convert to string
print("ord('A'):", ord('A'))                      # ASCII value
print("chr(65):", chr(65))                        # Character from ASCII
# ```

# **Output**:
# ```
# len(text): 15
# str(123): 123
# ord('A'): 65
# chr(65): A
# ```

## 2. String Case Methods

### Examples:
# ```python
text = "hello World"

print("text.upper():", text.upper())              # HELLO WORLD
print("text.lower():", text.lower())              # hello world
print("text.capitalize():", text.capitalize())    # Hello world
print("text.title():", text.title())              # Hello World
print("text.swapcase():", text.swapcase())        # HELLO wORLD
# ```

# **Output**:
# ```
# text.upper(): HELLO WORLD
# text.lower(): hello world
# text.capitalize(): Hello world
# text.title(): Hello World
# text.swapcase(): HELLO wORLD
# ```

## 3. String Search Methods

### Examples:
# ```python
text = "hello world hello"

print("text.find('world'):", text.find('world'))      # 6
print("text.index('world'):", text.index('world'))    # 6
print("text.rfind('hello'):", text.rfind('hello'))    # 12
print("text.count('hello'):", text.count('hello'))    # 2
print("'hello' in text:", 'hello' in text)            # True
print("text.startswith('hello'):", text.startswith('hello'))  # True
print("text.endswith('world'):", text.endswith('world'))      # False
# ```

# **Output**:
# ```
# text.find('world'): 6
# text.index('world'): 6
# text.rfind('hello'): 12
# text.count('hello'): 2
# 'hello' in text: True
# text.startswith('hello'): True
# text.endswith('world'): False
# ```

## 4. String Validation Methods

### Examples:
# ```python
text1 = "Hello123"
text2 = "12345"
text3 = "HELLO"
text4 = "hello"
text5 = "   "
text6 = "Hello World"

print("text1.isalnum():", text1.isalnum())        # True (letters and numbers)
print("text2.isdigit():", text2.isdigit())        # True (only digits)
print("text3.isupper():", text3.isupper())        # True (all uppercase)
print("text4.islower():", text4.islower())        # True (all lowercase)
print("text5.isspace():", text5.isspace())        # True (only whitespace)
print("text6.istitle():", text6.istitle())        # True (title case)
print("'abc'.isalpha():", 'abc'.isalpha())        # True (only letters)
# ```

# **Output**:
# ```
# text1.isalnum(): True
# text2.isdigit(): True
# text3.isupper(): True
# text4.islower(): True
# text5.isspace(): True
# text6.istitle(): True
# 'abc'.isalpha(): True
# ```

## 5. String Modification Methods

### Examples:
# ```python
text = "  hello world  "
names = "apple,banana,cherry"

print("text.strip():", text.strip())              # "hello world"
print("text.lstrip():", text.lstrip())            # "hello world  "
print("text.rstrip():", text.rstrip())            # "  hello world"
print("text.replace('world', 'Python'):", text.replace('world', 'Python'))
print("names.split(','):", names.split(','))      # ['apple', 'banana', 'cherry']
print("'-'.join(['a', 'b', 'c']):", '-'.join(['a', 'b', 'c']))  # a-b-c
# ```

# **Output**:
# ```
# text.strip(): hello world
# text.lstrip(): hello world  
# text.rstrip():   hello world
# text.replace('world', 'Python'):   hello Python  
# names.split(','): ['apple', 'banana', 'cherry']
# '-'.join(['a', 'b', 'c']): a-b-c
# ```

## 6. String Formatting Methods

### Examples:
# ```python
name = "John"
age = 25

# format() method
print("Hello {}, you are {} years old".format(name, age))
print("Hello {0}, you are {1} years old".format(name, age))
print("Hello {name}, you are {age} years old".format(name=name, age=age))

# f-strings (Python 3.6+)
print(f"Hello {name}, you are {age} years old")

# String formatting with alignment
print("'{:<10}'".format("left"))      # Left align
print("'{:>10}'".format("right"))     # Right align
print("'{:^10}'".format("center"))    # Center align
# ```

# **Output**:
# ```
# Hello John, you are 25 years old
# Hello John, you are 25 years old
# Hello John, you are 25 years old
# Hello John, you are 25 years old
# 'left      '
# '     right'
# '  center  '
# ```

## 7. String Translation Methods

### Examples:
# ```python
text = "hello world"
translation_table = str.maketrans('aeiou', '12345')

print("text.translate(translation_table):", text.translate(translation_table))
print("text.encode('utf-8'):", text.encode('utf-8'))
# ```

# **Output**:
# ```
# text.translate(translation_table): h2ll4 w4rld
# text.encode('utf-8'): b'hello world'
# ```

## 8. String Padding Methods

### Examples:
# ```python
text = "hello"

print("text.center(10, '*'):", text.center(10, '*'))  # **hello***
print("text.ljust(10, '-'):", text.ljust(10, '-'))    # hello-----
print("text.rjust(10, '+'):", text.rjust(10, '+'))    # +++++hello
print("text.zfill(10):", text.zfill(10))              # 00000hello
# ```

# **Output**:
# ```
# text.center(10, '*'): **hello***
# text.ljust(10, '-'): hello-----
# text.rjust(10, '+'): +++++hello
# text.zfill(10): 00000hello
# ```

## 9. String Partition Methods

### Examples:
# ```python
text = "hello.world.python"

print("text.partition('.'):", text.partition('.'))    # ('hello', '.', 'world.python')
print("text.rpartition('.'):", text.rpartition('.'))  # ('hello.world', '.', 'python')
print("text.splitlines():", "hello\nworld".splitlines())  # ['hello', 'world']
# ```

# **Output**:
# ```
# text.partition('.'): ('hello', '.', 'world.python')
# text.rpartition('.'): ('hello.world', '.', 'python')
# text.splitlines(): ['hello', 'world']
# ```

## 10. Advanced String Methods

### Examples:
#```python
text = "Hello World"

print("text.expandtabs(4):", "hello\tworld".expandtabs(4))  # hello   world
print("text.casefold():", "HELLO".casefold())              # hello (for case-insensitive comparisons)
print("text.removeprefix('Hello '):", text.removeprefix('Hello '))  # World
print("text.removesuffix('World'):", text.removesuffix('World'))    # Hello
# ```

# **Output**:
# ```
# text.expandtabs(4): hello   world
# text.casefold(): hello
# text.removeprefix('Hello '): World
# text.removesuffix('World'): Hello
# ```

# ## Complete Example with All Methods

# ```python
def demonstrate_string_methods():
    text = "  Hello World!  "
    
    print("Original:", repr(text))
    print("Upper:", text.upper())
    print("Lower:", text.lower())
    print("Strip:", repr(text.strip()))
    print("Replace:", text.replace('World', 'Python'))
    print("Find 'World':", text.find('World'))
    print("Count 'l':", text.count('l'))
    print("Starts with 'Hello':", text.startswith('Hello'))
    print("Is alphanumeric:", text.strip().isalnum())
    print("Split:", text.strip().split())
    print("Join:", '-'.join(['Hello', 'World']))

demonstrate_string_methods()
# ```

# **Output**:
# ```
# Original: '  Hello World!  '
# Upper:   HELLO WORLD!  
# Lower:   hello world!  
# Strip: 'Hello World!'
# Replace:   Hello Python!  
# Find 'World': 9
# Count 'l': 3
# Starts with 'Hello': False
# Is alphanumeric: False
# Split: ['Hello', 'World!']
# Join: Hello-World
# ```

## Key Points:
# - Strings are immutable - methods return new strings
# - Most string methods return a new string
# - Methods like `strip()`, `replace()`, `lower()` are very commonly used
# - String methods are essential for text processing and manipulation
# - Python provides over 40 built-in string methods for various operations