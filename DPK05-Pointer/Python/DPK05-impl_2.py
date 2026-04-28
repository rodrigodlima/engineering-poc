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


def play(name1, name2):
    winner = compare(name1, name2)

    if winner is None:  
        leaderboard[name1] += 5
        leaderboard[name2] += 5
    else:
        loser = name2 if winner == name1 else name1
        leaderboard[winner] += 10
        leaderboard[loser] -= 5

    return winner


print(play("John", "Paul"))
print(leaderboard)

print(play("John", "Ringo"))
print(leaderboard)
