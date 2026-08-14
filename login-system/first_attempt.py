# This program is a simple login system.
# The user enters a username and password.
# The correct username and password are both admin.
# The user has 4 attempts to log in.
# If the details are correct, the program prints WELCOME.

username = "admin"
password = "admin"

attempts = 0

while attempts < 4:
    user = input("Username: ")
    passw = input("Password: ")

    if user == username and passw == password:
        print("WELCOME")
        break
    else:
        print("Wrong username or password")
        attempts += 1

if attempts == 4:
    print("Access denied")