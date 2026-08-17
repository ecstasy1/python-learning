# Lesson 7: Operators and Expressions

## 1. What are Operators?

Operators are symbols or words that tell Python to perform an operation.

They can be used to:
- Do calculations
- Compare values
- Combine conditions
- Make decisions

The main types of operators in this lesson are:
- Arithmetic operators
- Comparison operators
- Logical operators

## 2. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

+ = addition
- = subtraction
* = multiplication
/ = division
** = exponent/power

Examples:

2 + 3 = 5
5 - 2 = 3
2 * 3 = 6
6 / 2 = 3.0
2 ** 3 = 8

Important: Python's / operator produces a float.

For example:

8 / 2 = 4.0

## 3. Arithmetic Example

milk_ounces = 16
pour_amount = 6

remaining = milk_ounces - pour_amount

print(remaining)

Output:
10

## 4. Comparison Operators

Comparison operators compare two values.

The result of a comparison is always True or False.

== = equal to
!= = not equal to
> = greater than
< = less than
>= = greater than or equal to
<= = less than or equal to

Examples:

5 == 5
Result: True

5 != 3
Result: True

5 > 3
Result: True

3 < 5
Result: True

5 >= 5
Result: True

3 <= 5
Result: True

## 5. = vs ==

These are different.

= is used to assign a value to a variable.

Example:

age = 18

This means we store 18 inside age.

== is used to compare two values.

Example:

age == 18

This checks whether age is equal to 18.

Remember:

= means assign

== means compare

## 6. Logical Operators

Logical operators are used to combine conditions.

The three logical operators are:

and
or
not

### and

and is True only when all conditions are True.

Example:

is_milk_fresh = True
is_cereal_fresh = True

can_serve = is_milk_fresh and is_cereal_fresh

print(can_serve)

Result:

True

If one condition is False, the result is False.

### or

or is True when at least one condition is True.

Example:

has_milk = True
has_cereal = False

can_eat = has_milk or has_cereal

print(can_eat)

Result:

True

Only one condition needs to be True.

### not

not reverses a boolean value.

True becomes False.

False becomes True.

Example:

is_fresh = True

print(not is_fresh)

Result:

False

## 7. Expressions

An expression is a combination of values, variables, and operators that produces a value.

Example:

cereal_scoops + 2

This produces a result.

Another example:

milk_ounces >= 8

This produces either True or False.

## 8. Combining Conditions

We can combine multiple comparisons using logical operators.

Example:

milk_ounces = 12
cereal_scoops = 4

ready = (milk_ounces >= 8) and (cereal_scoops >= 3)

print(ready)

Result:

True

Both conditions are True.

## 9. Operator Precedence

When Python sees several operators in one expression, it follows a specific order.

From highest priority to lowest:

1. ** = Exponentiation
2. * and / = Multiplication and Division
3. + and - = Addition and Subtraction
4. ==, !=, >, <, >=, <= = Comparisons
5. not
6. and
7. or

## 10. Parentheses

Parentheses can be used to control the order in which Python evaluates an expression.

Example:

print(2 + 3 * 4)

Python does multiplication first:

3 * 4 = 12

Then:

2 + 12 = 14

Result:

14

But:

print((2 + 3) * 4)

The parentheses make Python calculate:

2 + 3 = 5

Then:

5 * 4 = 20

Result:

20

## 11. Common Mistakes

### Mistake 1: Using = instead of ==

Incorrect:

if age = 18:

Correct:

if age == 18:

= assigns.

== compares.

### Mistake 2: Misunderstanding and

and requires every condition to be True.

Example:

has_milk and has_cereal

Both must be True.

### Mistake 3: Misunderstanding or

or requires at least one condition to be True.

### Mistake 4: Forgetting that / produces a float

Example:

8 / 2

Result:

4.0

Not:

4

## 12. Quick Summary

Arithmetic operators:

+ = addition
- = subtraction
* = multiplication
/ = division
** = exponent

Comparison operators:

== = equal
!= = not equal
> = greater than
< = less than
>= = greater than or equal to
<= = less than or equal to

Logical operators:

and = all conditions must be True
or = at least one condition must be True
not = reverses True and False

Important:

= assigns a value.

== compares values.

Python follows operator precedence when evaluating expressions.