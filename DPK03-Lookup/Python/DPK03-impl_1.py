def save_map(name, email):
    user_infos = {'name': name, "email": email}
    return user_infos


infos = save_map("Rodrigo", "rodrigodlima@gmail.com")
print(infos)