# Python Module 00 - 👤 Author: hdroliveira

![42 Porto](https://img.shields.io/badge/42-Porto-blue)
![Language](https://img.shields.io/badge/Language-Python%203-yellow)
![Score](https://img.shields.io/badge/Score-100%2F100-success)

**Python Module 00** is the starting point of the **Python for Data Science** track at 42. It serves as an introduction to the Python language, covering syntax basics, data structures, and the importance of writing clean, "Pythonic" code.

## 📂 Project Structure

This module consists of a series of exercises designed to get you comfortable with Python's core features.

| Exercise | Name | Description | Topic |
| :--- | :--- | :--- | :--- |
| **ex00** | Hello World | Basic environment setup and script execution. | Setup / Print |
| **ex01** | Exec | Reverse strings and handle command-line arguments. | Strings / `sys.argv` |
| **ex02** | Whois | Determine if a number is odd, even, or zero. | Conditionals |
| **ex03** | Text Analyzer | Count upper/lower case, punctuation, and spaces in text. | String Methods |
| **ex04** | Operations | Basic arithmetic operations with error handling. | Math / Exceptions |
| **ex05** | Kata | A series of small exercises to format strings and tuples. | Formatting / Tuples |
| **ex06** | Recipe | Create a cookbook using dictionaries (CRUD operations). | Dictionaries / Loops |
| **ex07** | Filterwords | Remove words shorter than *N* letters (using list comprehensions). | List Comprehensions |
| **ex08** | SOS | Encode a string into Morse code. | Dictionaries / Parsing |
| **ex09** | Guess | A simple "Guess the Number" game with random values. | Random / Loops |
| **ex10** | Loading | Create a progress bar using `yield` (generators). | Generators / Yield |

## 💡 Key Concepts

### Pythonic Code (PEP 8)
Unlike C, Python emphasizes code readability. This module enforces the **PEP 8** style guide.
- **Snake_case** for functions and variables.
- **Docstrings** for documenting modules and functions.
- **Indentation** (4 spaces) is mandatory.

### Virtual Environment
It is good practice to run your projects in an isolated environment to manage dependencies:
```bash
conda create -n 42AI python=3.7
conda activate 42AI

🛠️ Usage

Running Scripts
Python is an interpreted language, so no compilation is needed. Run the scripts directly:

python3 ex00/Hello.py

Example: Text Analyzer (ex03)
This exercise often requires using the python interactive shell or a main script.

from ex03.count import text_analyzer

text_analyzer("Python 2.0 was released in 2000.")
# Output:
# The text contains 32 characters:
# - 1 upper letter(s)
# - 23 lower letter(s)
# - 1 punctuation mark(s)
# - 5 space(s)

Example: Loading Bar (ex10)
Demonstrating the use of generators (yield) to create a memory-efficient progress bar.

# Inside loading.py
def ft_progress(lst):
    for i in lst:
        yield i

⚠️ Notes
Forbidden Functions: Typically, functions like quit() or exit() are discouraged in favor of proper control flow.

Error Handling: Inputs should be validated (e.g., checking if the user provided an integer where required).