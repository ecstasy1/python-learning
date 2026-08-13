# Lesson 5: Python Keywords and Syntax

## Lesson Overview

Python has rules that must be followed when writing code.

These rules are called syntax.

Python also has special words called keywords that already have a specific meaning.

If we break Python's syntax rules, Python will report an error.

This lesson covers:

- Python keywords
- Syntax
- Indentation
- Comments
- Built-in functions
- Syntax errors
- Indentation errors

---

## 1. Python Keywords

Keywords are special words that already have a specific meaning in Python.

Examples:

- `if`
- `else`
- `for`
- `while`
- `return`
- `class`
- `import`

Keywords cannot normally be used as variable names.

Example:

    if = 5

This is invalid because `if` is a Python keyword.

A valid variable name would be:

    my_if = 5

---

## 2. Syntax

Syntax means the rules for writing Python code correctly.

Python must follow these rules so that the interpreter can understand the program.

For example, an `if` statement needs a colon `:` at the end of the condition.

Correct:

    if age > 18:
        print("You are an adult")

Incorrect:

    if age > 18
        print("You are an adult")

The second example is missing the colon.

Python will report a `SyntaxError`.

---

## 3. Indentation

Indentation means the spaces at the beginning of a line.

Python uses indentation to show which code belongs to a block.

Correct:

    if age > 18:
        print("You are an adult")
        print("Welcome!")

Both `print()` statements are part of the `if` block because they have the same indentation.

Incorrect:

    if age > 18:
        print("You are an adult")
          print("Welcome!")

The second `print()` has incorrect indentation.

Python can report an `IndentationError`.

Important:

Python uses indentation as part of its syntax.

Indentation is not just for making code look neat.

---

## 4. Comments

A comment is a note written for humans.

Python ignores comments when running the program.

A comment starts with the `#` symbol.

Example:

    # This is a comment
    print("Hello")

Python ignores the comment and runs the `print()` statement.

Output:

    Hello

Comments can also be placed after code.

Example:

    print("Hello")  # This prints Hello

Comments are useful for explaining what code does.

---

## 5. Built-in Functions

Python provides many functions that we can use without creating them ourselves.

These are called built-in functions.

Examples:

    print()
    len()
    type()

### print()

Displays information in the terminal.

Example:

    print("Hello")

Output:

    Hello

### len()

Counts the number of items or characters.

Example:

    name = "Python"
    print(len(name))

Output:

    6

The word `Python` contains six characters.

### type()

Tells us the type of a value.

Example:

    name = "Python"
    print(type(name))

---

## 6. Keywords vs Built-in Functions

Keywords and built-in functions are not the same thing.

### Keywords

Keywords are special words that are part of Python's language syntax.

Examples:

    if
    else
    for
    while
    class
    return

### Built-in Functions

Built-in functions are functions Python provides for us to use.

Examples:

    print()
    len()
    type()

For example:

    if age > 18:
        print("Adult")

Here:

- `if` is a keyword.
- `print()` is a built-in function.

---

## 7. SyntaxError

A `SyntaxError` happens when Python's syntax rules are broken.

Example:

    if age > 18
        print("Adult")

The colon is missing.

Python cannot understand the statement correctly, so it produces a `SyntaxError`.

Simple meaning:

    SyntaxError = Python's writing rules were broken

---

## 8. IndentationError

An `IndentationError` happens when Python finds incorrect indentation.

Example:

    if age > 18:
        print("Adult")
          print("Welcome")

The second `print()` has incorrect indentation.

Python can report an `IndentationError`.

Simple meaning:

    IndentationError = the spaces at the beginning of the line are incorrect

---

## 9. Important Symbols and Rules

### Colon `:`

A colon is used after statements such as an `if` condition.

Example:

    if age > 18:
        print("Adult")

### Hash `#`

The `#` symbol starts a comment.

Example:

    # This is a comment

### Indentation

Spaces at the beginning of a line show that the line belongs to a block.

Example:

    if age > 18:
        print("Adult")

---

## 10. Examples

### Example 1: Keyword

    if age > 18:
        print("Adult")

`if` is a keyword.

### Example 2: Built-in Function

    print("Hello")

`print()` is a built-in function.

### Example 3: Comment

    # Python ignores this line
    print("Hello")

Output:

    Hello

### Example 4: Correct Indentation

    if age > 18:
        print("Adult")
        print("Welcome!")

### Example 5: Syntax Error

    if age > 18
        print("Adult")

The colon is missing.

### Example 6: Indentation Error

    if age > 18:
        print("Adult")
          print("Welcome!")

The indentation is incorrect.

---

## Key Things to Remember

1. A keyword is a special word that already has a meaning in Python.
2. Keywords cannot normally be used as variable names.
3. Syntax means the rules for writing Python code correctly.
4. An `if` statement requires a colon `:`.
5. Indentation shows which code belongs to a block.
6. Incorrect indentation can cause an `IndentationError`.
7. `#` starts a comment.
8. Python ignores comments when running the program.
9. `print()`, `len()`, and `type()` are built-in functions.
10. Built-in functions are different from keywords.
11. A `SyntaxError` means Python's syntax rules were broken.
12. An `IndentationError` means the indentation is incorrect.

---

## Quick Reference

Keyword
= special Python word

Syntax
= rules for writing Python code

Indentation
= spaces used to show code blocks

Comment
= note for humans that Python ignores

Built-in function
= function provided by Python

SyntaxError
= Python syntax rules were broken

IndentationError
= indentation is incorrect

if
= keyword

print()
= built-in function

len()
= built-in function

type()
= built-in function

#
= starts a comment

:
= used after statements such as an `if` condition