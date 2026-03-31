COUNTRIES = [
    ("Usa",     "English"),
    ("Brazil",  "Portuguese"),
    ("Spain",   "Spanish"),
    ("Italy",   "Italian"),
    ("France",  "French"),
    ("Germany", "German"),
]


def pattern_matcher(country: str) -> str:
    return next(lang for name, lang in COUNTRIES if name == country)


print(pattern_matcher("Usa")) 
print(pattern_matcher("Brazil"))  
print(pattern_matcher("Germany"))

