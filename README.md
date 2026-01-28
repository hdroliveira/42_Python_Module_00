# Growing Code - 👤 Author: hdroliveira

![42 Porto](https://img.shields.io/badge/42-Porto-blue)
![Language](https://img.shields.io/badge/Language-Python%203.10+-yellow)
![Style](https://img.shields.io/badge/Style-Flake8-green)

**Growing Code** is the introductory Python project at 42 (Piscine AI / Data Science). Using a "Community Garden" theme, this project introduces fundamental programming concepts, syntax, and the importance of writing clean functions.

## 📂 Project Structure

This project consists of 8 exercises (ex00 to ex07). The strict rule is to write **only functions**, handling input and output directly within them.

| Exercise | Name | Description | Topic |
| :--- | :--- | :--- | :--- |
| **ex00** | `ft_hello_garden` | Display a simple welcome message. | Basics / Print |
| **ex01** | `ft_plot_area` | Calculate area based on user input (width/length). | Variables / Math |
| **ex02** | `ft_harvest_total` | Sum harvest weights from 3 different days. | Accumulation |
| **ex03** | `ft_plant_age` | Check if a plant is ready to harvest (> 60 days). | Conditionals (If/Else) |
| **ex04** | `ft_water_reminder` | Reminder logic based on days since watering. | Conditionals logic |
| **ex05** | `ft_count_harvest` | Count days until harvest (Iterative & Recursive). | Loops vs Recursion |
| **ex06** | `ft_garden_summary` | Display a formatted summary of the garden status. | String Formatting |
| **ex07** | `ft_seed_inventory` | Manage inventory with specific units and **Type Hints**. | Type Annotations |

## 💡 Key Rules & Concepts

### 1. Functions Only
Unlike standard Python scripts, for this project:
* **Do NOT** use `if __name__ == "__main__":`.
* Each file must contain **only** the requested function.
* Input validation is not required (unless specified).

### 2. Recursion vs Iteration (ex05)
Exercise 5 requires implementing the same logic in two ways to understand the difference:
* `ft_count_harvest_iterative`: Uses standard loops (for/while).
* `ft_count_harvest_recursive`: Calls itself until a base condition is met.

### 3. Type Annotations (ex07)
Introduced in the final exercise, modern Python (3.10+) encourages specifying data types in function signatures for better code quality.

```python
# Example signature required for ex07
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    ...

🛠️ Usage & Testing

Helper main.py
The subject provides a main.py file to assist with testing, as we cannot include main blocks in our submitted files.

Place main.py in the root of your working directory.

Run the tester:
python3 main.py

Manual Testing
You can also create your own temporary tester:

# test_ex07.py
from ex07.ft_seed_inventory import ft_seed_inventory

ft_seed_inventory("tomato", 15, "packets")
# Output: Tomato seeds: 15 packets available

Run with:

python3 test_ex07.py

⚠️ Notes
Linter: Code must respect flake8 standards.

Version: Strictly Python 3.10 or higher.

Formatting: Pay attention to exact output strings (e.g., "Status: Growing well!").