# Lesson 7 Challenge

## 1. What is an arithmetic operator?

Explain in your own words.

it is used to carry out mathematical operation


## 2. What does each of these operators do?

+ adds
- subtracts
* multiplies
/ divides
** exponent/power


## 3. What is the difference between = and ==?

Explain in your own words.

= assigns while == compares


## 4. What is the result of each?

a. 15 + 5 = 20

b. 20 - 8 = 12

c. 6 * 4 = 24

d. 20 / 5 = 4.0

e. 2 ** 5 = 32


## 5. What are comparison operators used for?

Explain in your own words.

comaparison operators are used to compare two values and the result coulde either true or false


## 6. What will each produce?

a. 10 > 5 = true

b. 10 < 5 = false

c. 10 == 10  true

d. 10 != 10 false

e. 10 >= 10 true

f. 5 <= 3 false


## 7. Explain the three logical operators.

What do:

and
or
not

do?

and is True only when all conditions are True.
or is True when at least one condition is True.
not reverses a boolean value

## 8. What will each produce?

a. True and False = false

b. True or False =  true

c. not True = false


## 9. What is an expression?

Explain in your own words.

An expression is a combination of values, variables and operators that produce a value


## 10. What is operator precedence?

Explain what it tells Python to do.

It tells python what to calculate first


## 11. What will this produce?

2 + 3 * 4

14

Explain why.

on the list of python operator precedence * comes before +


## 12. What will this produce?

(2 + 3) * 4

20

Explain why the answer is different from Question 11.


The parentheses tell Python to calculate 2 + 3 first.


## 13. Combining conditions

Given:

age = 20
has_id = True

What will this produce?

age >= 18 and has_id == True

Explain why.

True, because age >= 18 is True and has_id == True is also True. Since and requires both conditions to be True, the final result is True.


## 14. Write your own example

Create two variables and use and to combine two conditions.

age = 20
has_id = True

print(age >= 18 and has_id == True)


## 15. Write your own example

Create two variables and use `or` to combine two conditions.

Your example should show that `or` is True when at least one condition is True.


has_cash = False
has_card = True

print(has_cash or has_card)