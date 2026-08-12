# Lesson 4 Challenge

## 1. What is an interpreter? 
a programme that reads translates and executes as it runs

## 2. What is a compiler?
a it translates an entire program before it executes

## 3. What is the difference between an interpreter and a compiler?
An interpreter translates and executes code as it runs, while a compiler translates the entire program before it executes.
## 4. How does Python normally execute code?
fom top to bottom line by line, from top to bottom

## 5. What happens when Python encounters an error?
it stops at the error, prints it out and does not go ahead with the rest of the program

## 6. What does `print()` do?
displays output in the terminal

## 7. What does `>` do in the terminal?
> redirects program output into a file. It creates the file if it doesn't exist and overwrites it if it does.

## 8. What does `cat` do?
displays the content of a file in a terminal

## 9. What does `echo $?` show?
success or failure of previous command

## 10. What does an exit status of `0` mean?
success
## 11. What does `&&` do?
dunno how to put it...more link print it worked if prvious command was sucessful

## 12. What does `||` do?
prints it is a failure if previous command failed to run

## 13. What is the difference between `>` and `>>`?
> redirects output and overwrites the file, while >> redirects output and adds it to the end of the file.

## 14. What is stdout?
standard output

## 15. What is stderr?
standard error

## 16. Why did this command print "It worked!"?
```bash
python3 execution.py && echo "It worked!"

execution.py ran successfully, so its exit status was 0. Because && means "run the next command if the previous command succeeds," echo "It worked!" was executed.


## 17.Why did this command print "It failed!"?
python3 missing.py || echo "It failed!"

missing.py does not exist, so the first command failed. Because || runs the next command when the first command fails, "It failed!" was printed.

## 18. What did you learn?
I learned that > redirects output and >> appends output to a file
