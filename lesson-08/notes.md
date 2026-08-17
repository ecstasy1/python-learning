# Lesson 8: Type Casting

## What is Type Casting?

Type casting means changing a value from one data type to another.

Python has different data types such as:

- int → whole numbers
- float → decimal numbers
- str → text
- bool → True or False

Sometimes we need to change one type into another so Python can perform the operation we want.

## 1. int()

`int()` converts a value into a whole number.

Example:

number = int("2")

The string "2" becomes the integer 2.

print(number)
print(type(number))

Output:
2
<class 'int'>

## 2. float()

`float()` converts a value into a decimal number.

Example:

number = float("1.5")

The string "1.5" becomes the float 1.5.

print(number)
print(type(number))

Output:
1.5
<class 'float'>

## int() and Decimals

We should not use `int()` to convert a string containing a decimal.

int("1.5")

This causes a ValueError because "1.5" is not a whole number.

Instead, use:

float("1.5")

## 3. str()

`str()` converts a value into text.

Example:

age = 18
message = "I am " + str(age) + " years old."

print(message)

Output:
I am 18 years old.

`str(18)` changes the integer 18 into the string "18".

This allows us to combine the number with other text.

## Why Type Casting Is Important

Sometimes Python receives information as text, but we need to use it as a number.

For example:

banana_count = "2"
milk_cups = "1.5"

These are both strings.

If we do:

total = banana_count + milk_cups

Python joins the strings instead of doing mathematical addition.

The result is:

"21.5"

To perform actual mathematics, we need to convert them:

banana_count = int("2")
milk_cups = float("1.5")

total = banana_count + milk_cups

print(total)

The result is:

3.5

## Conversion Errors

A conversion error happens when Python cannot make the requested conversion.

For example:

number = int("banana")

Python cannot turn the word "banana" into a whole number, so it produces a ValueError.

## .isdigit()

`.isdigit()` can check whether a string contains only digits.

Example:

value = "15"
print(value.isdigit())

Output:
True

But:

value = "banana"
print(value.isdigit())

Output:
False

We can use this check before converting text to an integer.

Example:

value = "15"

if value.isdigit():
    number = int(value)
    print("Conversion successful!")
else:
    print("That is not a valid number.")

## Important Things to Remember

int() → converts to a whole number

float() → converts to a decimal number

str() → converts to text

.isdigit() → checks whether a string contains only digits

Type casting → changing a value from one data type to another

A conversion can fail if the value cannot be converted into the requested type.

## Quick Examples

int("10") → 10

float("2.5") → 2.5

str(25) → "25"

"10" + "5" → "105"

10 + 5 → 15