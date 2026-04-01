COUNTRIES = [
    ("Usa", "English"),
    ("Brasil", "Portuguese"),
    ("Spain", "Spanish"),
    ("Italy", "Italian"),
    ("France", "French"),
    ("Germany", "German")
]


def pattern_matcher(country: str) -> str:
    return next(filter(lambda x: x[0] == country, COUNTRIES))[1]


print(pattern_matcher("Usa"))