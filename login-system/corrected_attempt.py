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