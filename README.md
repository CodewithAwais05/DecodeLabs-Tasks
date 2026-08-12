# DecodeLabs Python Programming Internship

Python projects completed during my **1-month remote internship at DecodeLabs**,
under the **Industrial Training Kit (Batch 2026)** — Python Programming track.

Each project is a small, self-contained backend script designed to build core
programming skills step by step, following an **Input → Process → Output**
model with an emphasis on clean, defensive coding.

---

## 📁 Projects

### Project 1 — To-Do List
A command-line task manager that lets the user add, view, and remove tasks.
Demonstrates list manipulation, loop-based menus, and basic program flow
control.

**Run:**
```bash
python "Project 1(To-Do_List)/todo_list.py"
```

---

### Project 2 — Expense Tracker
Continuously accepts expense amounts from the user and keeps a running
total using the **accumulator pattern**. Validates input with
`try/except` and exits cleanly using a sentinel value (`quit`).

**Key concepts:** state persistence, accumulator pattern, exception
handling, sentinel-controlled loops.

**Run:**
```bash
python "Project 2(Expense Tracker)/expense_tracker.py"
```

**Example:**
```
Enter an expense amount (or 'quit' to stop): 100
Enter an expense amount (or 'quit' to stop): 50
Enter an expense amount (or 'quit' to stop): quit
Total Spent: 150
```

---

### Project 3 — Random Password Generator
Asks the user for a desired password length and generates a
cryptographically secure random password using letters and numbers.

**Key concepts:** the `string` and `secrets` modules, secure randomness
(`secrets.choice()` over `random.choice()`), efficient string building
with `''.join()`.

**Run:**
```bash
python "Project 3(Password Generator)/password_generator.py"
```

**Example:**
```
Enter the desired password length (e.g., 8): 12
Generated Password: dI3kbasKlIb3
```

---

## 🛠 Tech Stack
- **Language:** Python 3
- **Modules used:** `string`, `secrets`

## 🎯 What This Repo Demonstrates
- Core Python fundamentals (loops, conditionals, functions)
- Defensive coding and input validation
- State management across program execution
- Secure coding practices (cryptographically safe randomness)
- Clean, readable code structured for real-world backend logic

## 📄 License
This repository is licensed under the MIT License — see [LICENSE](LICENSE)
for details.

## 👤 Author
**Muhammad Awais Raza**
Remote Python Programming Intern — DecodeLabs (Batch 2026)