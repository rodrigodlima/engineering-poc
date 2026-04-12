users = {
    1: {"name": "John", "email": "john@john.jhon.com"},
}


def lookup(key):
    if isinstance(key, int):
        if key in users:
            return users[key]["name"]
        return None

    for user in users.values():
        if user["name"] == key:
            return user["email"]
        if user["email"] == key:
            return user["name"]

    return None

print(lookup(1))                      
print(lookup("John"))                 
print(lookup("john@john.jhon.com"))  