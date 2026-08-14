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