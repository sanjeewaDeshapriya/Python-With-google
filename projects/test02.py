def get_username():
    name = input("name:")
    return name

username = get_username()

while "abc"!=username:
    print("Invalid username")
    username = get_username()