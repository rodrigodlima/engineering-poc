# Simple Engineering Problems

## Rationale

A list of engineering problems worth solving.

- Helps engineers understand what they are doing
- Helps to build confidence
- Helps to build up coding skills
- Helps to build up debugging skills

## How to Use

- Can be done with any language
- Do it **2h per day, every day** no matter what — could be any time, but do it
- **2h per day is critical — it must be daily**
- Understand the code line by line

### The 4 Things to Always Do

1. **Table test** ("Teste de mesa") — simulate code execution in a text block file
2. **Debug** the code to understand it
3. **Ask questions**
4. **Make sure you understand every single line** of the code

### Rules

- Each problem should be done **10 times** before moving to the next one
- It's okay to copy on the first time
- All other times: done **without looking at the solution**
- If stuck, you can look at the solution — but **no more than 3 times**

### Expected File Structure

```
src/DPK01_impl_1.js
src/DPK01_impl_2.js
src/DPK01_impl_3.js
src/DPK01_impl_4.js
src/DPK01_impl_5.js
src/DPK01_impl_6.js
src/DPK01_impl_7.js
src/DPK01_impl_8.js
src/DPK01_impl_9.js
src/DPK01_impl_10.js
```

> All files may have the same code — that's fine. What matters is practice. You might find better ways of doing it, but if you don't, that's also fine.

### How to Present Each Solution

1. Explain the problem
2. Explain the solution line by line
3. Share the parts that were hard to understand — ask for advice
4. Ask for refactoring tips — how could the code be better?
5. Ask for feedback

---

## Problems

### DPK01 — Revert String

Create a function that reverts a string.

```
revert("Hello") -> "olleH"
```

---

### DPK02 — Revert a List

Create a function that reverts a list.

```
revert([1,2,3,4,5]) -> [5,4,3,2,1]
```

---

### DPK03 — Lookup

Create a function that performs a lookup in a map for a given key. Should have `id` and `name`.

```
lookup(1) -> "John"
```

Refactor so you can lookup by email as well, returning name and vice versa.

```
lookup("John")               -> "john@john.jhon.com"
lookup("john@john.jhon.com") -> "John"
```

---

### DPK04 — Simple Pattern Matcher

Given the following countries and languages:

| Country | Language   |
|---------|------------|
| Usa     | English    |
| Brazil  | Portuguese |
| Spain   | Spanish    |
| Italy   | Italian    |
| France  | French     |
| Germany | German     |

Create a function that returns the language for a given country. **Cannot use a hashmap or dictionary.**

```
pattern_matcher("Usa") -> "English"
```

Refactor: can you do that **without using IF statements**?

```
pattern_matcher("Usa") -> "English"
```

---

### DPK05 — Pointers

Given:

```
power = {
  "John":   100,
  "Paul":   90,
  "George": 80,
  "Ringo":  70
}
```

Create three functions:

1. Returns the power of a given person
2. Receives 2 names and returns which one is most powerful (uses function 1)
3. Receives 2 names and updates the leaderboard

Leaderboard starts at:

```
leaderboard = {
  "John":   0,
  "Paul":   0,
  "George": 0,
  "Ringo":  0
}
```

**Scoring:** win = `+10`, draw = `+5` each, loss = `-5`

```
play("John", "Paul") -> "John"
leaderboard -> { "John": 10, "Paul": -5, "George": 0, "Ringo": 0 }

play("John", "Ringo") -> "John"
leaderboard -> { "John": 20, "Paul": -5, "George": 0, "Ringo": -5 }
```

Refactor: fewer IFs. Maybe introduce pointers?

---

### DPK06 — Tokenizer

Create a function that tokenizes a string based on a token.

```
tokenize("Hello,World,How,Are,You", ",") -> ["Hello", "World", "How", "Are", "You"]
tokenize("Hello World How Are You", " ") -> ["Hello", "World", "How", "Are", "You"]
tokenize("Hello-World-How-Are-You", "-") -> ["Hello", "World", "How", "Are", "You"]
```

Refactor: **do not use any prebuilt function** like `split`.

---

### DPK07 — Group By

Create a function that groups a list by a given size.

```
group_by([1,2,3,4,5,6,7,8,9,10], 3) -> [[1,2,3], [4,5,6], [7,8,9], [10]]
```

Must also work with strings:

```
group_by(["a","b","c","d","e","f","g","h","i","j"], 3) -> [["a","b","c"], ["d","e","f"], ["g","h","i"], ["j"]]
```

Refactor: **do not use any prebuilt function**.

---

### DPK08 — Map

Create a function that maps a function to each element of a list and returns a new list.

```
map([1,2,3,4,5], (x) => x * 2) -> [2,4,6,8,10]
```

Receives a collection and a function applied to each element.

Refactor: **do not use any prebuilt function**.

---

### DPK09 — Filter

Create a function that filters a list based on a condition.

```
filter([1,2,3,4,5,6,7,8,9,10], (x) => x % 2 == 0) -> [2,4,6,8,10]
```

Receives a collection and a predicate function.

Refactor: **do not use any prebuilt function**.

---

### DPK10 — Reduce

Create a function that reduces a list to a single value.

```
reduce([1,2,3,4,5], (acc, x) => acc + x, 0) -> 15
```

Receives a collection, a function, and an initial value.

Refactor: **do not use any prebuilt function**.

---

### DPK11 — Replace

Create a function that replaces a given token in a string.

```
replace("Hello,World,How,Are,You", ",", "-") -> "Hello-World-How-Are-You"
```

Refactor to replace not just single characters but substrings:

```
replace("Hello,World,How,Are,You", ",World,", "-") -> "Hello-How-Are-You"
```

Refactor: **do not use any prebuilt function**.

---

### DPK12 — Sort

Create a function that sorts a list of numbers using **Bubble Sort** (good to learn, terrible in production).

```
bubble_sort([5,4,3,2,1]) -> [1,2,3,4,5]
```

Receives a collection and returns a new sorted list.

---

### DPK13 — FizzBuzz

Create a function that returns a list of numbers from 1 to 100. For multiples of 3 return `"Fizz"`, multiples of 5 return `"Buzz"`, multiples of both return `"FizzBuzz"`.

```
fizzbuzz() -> [1,2,"Fizz",4,"Buzz","Fizz",7,8,"Fizz","Buzz",11,"Fizz",13,14,"FizzBuzz", ...]
```

Refactor to receive the count as a parameter:

```
fizzbuzz(10) -> [1,2,"Fizz",4,"Buzz","Fizz",7,8,"Fizz","Buzz"]
```

---

### DPK14 — 2D Walk

Create a function that moves a fighter on a 2D grid.

```
grid = [
  ["Ryu",  "E.Honda", "Blanka",  "Guile",  "Balrog", "Vega"  ],
  ["Ken",  "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]
```

**Moves:** `up`, `down`, `left`, `right`

Receives the grid, initial position, and a list of moves. Every time a player moves to a new position, the old position becomes empty.

```
move(grid, [0,0], ["up"]) ->
  ["", "E.Honda", "Blanka", "Guile", "Balrog", "Vega",
   "Ryu", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
```

Returns a list of all players that were beaten (removed from the grid):

```
move(grid, [0,0], ["up", "left", "down", "right"]) -> ["Ken", "M.Bison", "Vega"]
```

---

### DPK15 — OOP with Classes

Create a class representing a person with name, age, and a list of friends.

```
person = new Person("John", 30)
person.addFriend("Paul")
person.addFriend("George")
person.addFriend("Ringo")

person.getFriends() -> ["Paul", "George", "Ringo"]
person.getAge()     -> 30
person.getName()    -> "John"
```

**Refactoring steps:**

1. Move the list of friends to a separate class
2. Disallow adding the same friend twice
3. Add ability to remove a friend

**More refactoring:**

- Method: who is the person with the most friends?
- Method: who is the person with the least friends?
- Method: who is the person with the oldest friend?

---

### DPK16 — Mosquito Game

Create the following classes: `Exterminator`, `Mosquito`, `Game`

**Rules:**

- Game starts with **10 mosquitos** and **1 exterminator**
- Internal matrix: **100×100**
- Every 1s: mosquito moves to a random position
- Every 1s: exterminator moves to a specific position
- If mosquito and exterminator share a position → mosquito dies
- If mosquito moves **5 times without being killed** → it reproduces if a nearby mosquito exists
- Mosquito moves: up, down, left, right, diagonals
- Exterminator sweeps the matrix: bottom-left → top-right → back on same route

**Methods:**

- Return number of mosquitos killed
- Return number of mosquitos alive

> No UI needed — print the matrix to the console.
