power = {
    "John": 100,
    "Paul": 90,
    "George": 80,
    "Ringo": 70
}

leaderboard = {
    "John": 0,
    "Paul": 0,
    "George": 0,
    "Ringo": 0
}


def get_power(name):
    return power[name]


def compare(name1, name2):
    power1 = get_power(name1)
    power2 = get_power(name2)

    if power1 > power2:
        return name1
    elif power2 > power1:
        return name2
    else:
        return None

