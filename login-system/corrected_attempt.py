# This is my corrected login system.
# The username must be correct before the password is requested.
# If the username is wrong, it asks for the username again.
# If the password is wrong, it asks for the password again.
# Username and password share 4 total attempts.
# If the login is correct, the program prints WELCOME.

username = "admin"
password = "admin"

attempts = 0

while attempts < 4:
    user = input("Enter username: ")

    if user == username:
        break

    attempts += 1
    print("Wrong username")

if attempts == 4:
    print("Access denied")

else:
    while attempts < 4:
        user_password = input("Enter password: ")

        if user_password == password:
            print("WELCOME")
            break

        attempts += 1
        print("Wrong password")

    if attempts == 4:
        print("Access denied")