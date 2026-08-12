# Lesson 4: How Python Runs Your Code

## 1. Interpreter

An interpreter is a program that reads, translates, and executes code as the program runs.

Python is an interpreted language.

Python generally executes code from top to bottom.

Example:

print("First")
print("Second")
print("Third")

Output:

First
Second
Third

If Python encounters an error, it stops at that point and does not execute the lines after the error.

---

## 2. Compiler

A compiler translates an entire program before the program is executed.

Simple difference:

- Interpreter: translates and executes code as the program runs.
- Compiler: translates the whole program before execution.

---

## 3. Execution Order

Python normally executes instructions from top to bottom.

Example:

print("First")
print("Second")
print("Third")

Python runs:

1. First
2. Second
3. Third

If an error occurs on a line, Python stops there.

---

## 4. print()

The `print()` function displays information in the terminal.

Example:

print("Hello")

Output:

Hello

Text must be inside quotation marks.

The parentheses must also be closed.

---

## 5. Output Redirection `>`

Normally, Python sends output to the terminal:

python3 execution.py

We can redirect the output into a file using `>`:

python3 execution.py > output.txt

This sends the program's output into `output.txt` instead of displaying it on the screen.

We can view the file using:

cat output.txt

Important:

`>` overwrites the contents of the file if the file already exists.

---

## 6. Exit Status

Every command returns an exit status when it finishes.

We can check the exit status using:

echo $?

The basic rule is:

- `0` = success
- Non-zero = failure

Example:

python3 execution.py
echo $?

If the program succeeds:

0

If something goes wrong, a non-zero number is returned.

---

## 7. Command Chaining with `&&`

`&&` means:

Run the next command only if the first command succeeds.

Example:

python3 execution.py && echo "It worked!"

If `execution.py` succeeds, the second command runs.

Think:

SUCCESS → continue

---

## 8. Command Chaining with `||`

`||` means:

Run the next command only if the first command fails.

Example:

python3 missing.py || echo "It failed!"

If `missing.py` does not exist, the first command fails and the second command runs.

Think:

FAILURE → fallback

---

## 9. `>` vs `>>`

`>` redirects output into a file and overwrites the existing contents.

Example:

python3 execution.py > output.txt

`>>` redirects output and adds it to the end of the existing file.

Example:

python3 execution.py >> output.txt

Simple difference:

`>` = overwrite

`>>` = append

---

## 10. Standard Output (stdout)

`stdout` means standard output.

It is the normal output produced by a program.

For example:

print("Hello")

The `"Hello"` is normal output.

---

## 11. Standard Error (stderr)

`stderr` means standard error.

It is used for error messages and error information.

For example, if Python encounters a `NameError`, the error message is sent through stderr.

Normal output and errors are separate streams.

---

## 12. Important Commands Learned

`python3 execution.py`

Runs a Python program.

`cat output.txt`

Displays the contents of a file.

`echo $?`

Shows the exit status of the previous command.

`python3 execution.py > output.txt`

Redirects output into a file.

`python3 execution.py >> output.txt`

Appends output to a file.

`command1 && command2`

Runs command2 only if command1 succeeds.

`command1 || command2`

Runs command2 only if command1 fails.

---

## Key Things to Remember

1. Python is an interpreted language.
2. Python normally executes code from top to bottom.
3. `print()` displays output.
4. `>` redirects output and overwrites a file.
5. `>>` redirects output and appends to a file.
6. `echo $?` checks the previous command's exit status.
7. `0` means success.
8. A non-zero exit status means failure.
9. `&&` means continue if successful.
10. `||` means run a fallback if the command fails.
11. `stdout` is normal program output.
12. `stderr` is used for error messages.