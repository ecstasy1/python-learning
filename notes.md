# Lesson 6: Variables and Primitive Types

## Lesson Overview

Variables are used to store information in a Python program.

Think of a variable like a labeled storage jar. The label tells us what is inside the jar, while the value is the information stored in it.

This lesson covers:

- Variables
- Assignment
- The `=` operator
- Data types
- `int`
- `float`
- `str`
- `bool`
- The `type()` function
- Changing variable values
- Dynamic typing
- Common variable mistakes

---

## 1. Variables

A variable is a named container used to store information.

Example:

```python
bean_count = 15
````

Here:

* `bean_count` is the variable name.
* `=` is the assignment operator.
* `15` is the value stored in the variable.

Think of it as:

```text
bean_count → 15
```

---

## 2. Assignment

Assignment means putting a value into a variable.

The assignment operator is:

```text
=
```

The basic pattern is:

```text
variable = value
```

Example:

```python
bean_count = 15
```

The variable goes on the left, and the value goes on the right.

---

## 3. Correct and Incorrect Assignment

Correct:

```python
bean_count = 15
```

Incorrect:

```python
15 = bean_count
```

The variable must be on the left side of `=`.

Remember:

```text
variable = value
```

---

## 4. The Four Primitive Types

Python has four basic data types introduced in this lesson:

1. `int`
2. `float`
3. `str`
4. `bool`

---

## 5. Integer (`int`)

An integer is a whole number.

Examples:

```python
bean_count = 15
age = 25
quantity = 3
```

These are integers because they do not contain decimal points.

Example:

```python
age = 25
print(type(age))
```

Output:

```text
<class 'int'>
```

Remember:

```text
25 → int
100 → int
3 → int
```

---

## 6. Float (`float`)

A float is a number containing a decimal value.

Examples:

```python
water_cups = 1.5
price = 14.99
temperature = 25.5
```

Example:

```python
price = 14.99
print(type(price))
```

Output:

```text
<class 'float'>
```

Remember:

```text
25 → int
25.5 → float
```

---

## 7. String (`str`)

A string is text.

Strings are written inside quotation marks.

Examples:

```python
name = "Ecstasy"
roast_level = "Medium Dark"
message = "Hello"
```

Example:

```python
name = "Python"
print(type(name))
```

Output:

```text
<class 'str'>
```

You can use either single or double quotes:

```python
name = "Ecstasy"
name = 'Ecstasy'
```

---

## 8. Boolean (`bool`)

A Boolean represents one of two values:

```text
True
False
```

Examples:

```python
is_caffeinated = True
is_finished = False
is_learning = True
```

Example:

```python
is_learning = True
print(type(is_learning))
```

Output:

```text
<class 'bool'>
```

Remember:

```text
True → bool
False → bool
```

`True` and `False` begin with capital letters.

---

## 9. Comparing the Four Types

Example:

```python
bean_count = 15
water_cups = 1.5
roast_level = "Medium Dark"
is_caffeinated = True
```

Their types are:

```text
bean_count → int
water_cups → float
roast_level → str
is_caffeinated → bool
```

Easy way to remember:

```text
int   → whole numbers
float → decimal numbers
str   → text
bool  → True or False
```

---

## 10. Checking Types with `type()`

Python has a built-in function called `type()`.

It tells us what type of value a variable contains.

Example:

```python
bean_count = 15
water_cups = 1.5
roast_level = "Medium Dark"
is_caffeinated = True

print(type(bean_count))
print(type(water_cups))
print(type(roast_level))
print(type(is_caffeinated))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

---

## 11. Quotes Change the Data Type

Quotation marks are important.

This:

```python
price = 14.99
```

creates a float.

But this:

```python
price = "14.99"
```

creates a string.

Remember:

```text
14.99 → float
"14.99" → str
```

The quotation marks tell Python to treat the value as text.

---

## 12. Changing a Variable's Value

A variable's value can be changed.

Example:

```python
score = 100
score = 75
```

The final value of `score` is:

```text
75
```

The second assignment replaces the first value.

Another example:

```python
age = 25
age = 30

print(age)
```

Output:

```text
30
```

Python uses the most recent value assigned to the variable.

---

## 13. Variables Can Change Type

Python is dynamically typed.

This means you do not have to explicitly declare the type of a variable before using it.

A variable can be assigned a different type later.

Example:

```python
age = 25
```

At this point:

```text
age → int
```

Then:

```python
age = "twenty-five"
```

Now:

```text
age → str
```

Python determines the type from the value currently stored in the variable.

---

## 14. Variable Names

Variable names should clearly describe the information they store.

Good examples:

```python
age = 25
bean_count = 15
water_cups = 1.5
roast_level = "Medium Dark"
```

When a variable name contains multiple words, underscores can be used.

Example:

```python
bean_count = 15
```

This style is called `snake_case`.

---

## 15. Variable Names Cannot Contain Spaces

Incorrect:

```python
bean count = 15
```

Python does not allow spaces inside variable names.

Correct:

```python
bean_count = 15
```

Another example:

```python
first_name = "Ecstasy"
```

---

## 16. Common Mistake: Putting Quotes Around Numbers

Incorrect:

```python
bean_weight = "12.5"
```

This is a string.

Correct:

```python
bean_weight = 12.5
```

This is a float.

Remember:

```text
"12.5" → str
12.5 → float
```

---

## 17. Common Mistake: Reversing Assignment

Incorrect:

```python
15 = bean_count
```

Correct:

```python
bean_count = 15
```

The variable goes on the left side of `=`.

The value goes on the right side.

---

## 18. Real-World Application

Variables and primitive types are used in real applications such as shopping apps.

Example:

```python
item_quantity = 3
item_price = 14.99
promo_code = "COFFEE20"
free_shipping_applied = True
```

The types are:

```text
item_quantity → int
item_price → float
promo_code → str
free_shipping_applied → bool
```

Different data types allow programs to represent different kinds of information.

For example:

* `int` can represent quantities.
* `float` can represent prices.
* `str` can represent names or promo codes.
* `bool` can represent whether something is true or false.

---

## 19. Why Data Types Matter

Different types of data behave differently.

For example:

```python
price = 14.99
```

is a number, so Python can perform mathematical operations with it.

But:

```python
price = "14.99"
```

is text.

The quotation marks tell Python that the value is a string.

Therefore, storing information using the correct data type is important.

---

## 20. Dynamic Typing

Python uses dynamic typing.

Python determines the data type from the value assigned to a variable.

Example:

```python
value = 10
```

Here:

```text
value → int
```

Then:

```python
value = "Hello"
```

Now:

```text
value → str
```

We did not have to explicitly declare the type.

Python determines it automatically.

---

## 21. Quick Type Reference

```text
int
= whole numbers

Example:
age = 25
```

```text
float
= decimal numbers

Example:
price = 14.99
```

```text
str
= text

Example:
name = "Ecstasy"
```

```text
bool
= True or False

Example:
is_learning = True
```

---

## 22. Complete Example

```python
name = "Ecstasy"
age = 25
price = 14.99
is_learning = True

print(name)
print(age)
print(price)
print(is_learning)

print(type(name))
print(type(age))
print(type(price))
print(type(is_learning))
```

Expected output:

```text
Ecstasy
25
14.99
True
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

---

## 23. Key Things to Remember

1. A variable stores information.
2. A variable has a name and a value.
3. The assignment operator is `=`.
4. The variable goes on the left side of `=`.
5. The value goes on the right side of `=`.
6. `int` means a whole number.
7. `float` means a decimal number.
8. `str` means text.
9. `bool` means `True` or `False`.
10. Quotes turn values such as `"14.99"` into strings.
11. `type()` checks the data type of a value.
12. A variable's value can be changed.
13. Python is dynamically typed.
14. Variable names cannot contain spaces.
15. Underscores can be used to separate words in variable names.

---

## Quick Summary

```text
Variable
A named container used to store information.

Assignment
Putting a value into a variable.

=
Assignment operator.

int
Whole number.

float
Decimal number.

str
Text.

bool
True or False.

type()
Checks the data type of a value.

Dynamic typing
Python automatically determines the type of a value when it is assigned.
```

## Most Important Pattern

Always remember:

```python
variable = value
```

Examples:

```python
name = "Ecstasy"
age = 25
price = 14.99
is_learning = True
```

These create four variables with four different primitive types.

