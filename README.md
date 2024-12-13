# Lab 10: Unit Testing and Flask To-Do List Application

## **Overview**
This repository contains the implementation and unit testing of various functions and a Flask-based "To-Do List" application as per the requirements of Lab 10. The lab emphasizes unit testing, extending functionality, encapsulating logic into a class, and building a simple web application.

---

## **Requirements**

### **1. Unit Testing**

#### **1.1 Write Unit Tests from Scratch**
- **Function 1:** `multiply_numbers(a, b)`
  - A function to multiply two numbers. Test cases include:
    - Two positive numbers.
    - Multiplication with zero.
    - Negative numbers.
- **Function 2:** `reverse_list(input_list)`
  - A function to reverse a given list. Test cases include:
    - A normal list.
    - An empty list.
    - A single-element list.

#### **1.2 Extend Provided Code**
- **Function 3:** `calculate_discount(price, discount_percentage)`
  - Enhancements:
    - Test for valid inputs (e.g., price = 100, discount = 10%).
    - Test for invalid discounts (e.g., negative or greater than 100%).
    - Handle zero price or zero discount gracefully.

#### **1.3 Encapsulate in a Class**
- **Class:** `MathOperations`
  - **Method 1:** `is_prime(n)`
    - Checks if a number is prime.
    - Test cases:
      - Prime numbers.
      - Non-prime numbers.
      - Edge cases (0, 1, negative numbers).
  - **Method 2:** `factorial(n)`
    - Computes the factorial of a number.
    - Test cases:
      - Positive integers.
      - Edge case: n = 0 (factorial is 1).
      - Invalid cases: negative numbers.

---

### **2. Flask-Based To-Do List Application**

#### **Backend Requirements**
- **In-memory list:** `tasks` to store task descriptions.
- **Functions:**
  - `add_task(task)` – Adds a task to the `tasks` list.
  - `get_tasks()` – Returns the current list of tasks.
- **Flask Routes:**
  - `/` – Displays an HTML page with:
    - A form to submit new tasks.
    - A list of all current tasks.
  - `/add-task` – Handles POST requests to:
    - Add a task using `add_task(task)`.

#### **Frontend Requirements**
- **HTML Page:** `index2.html`
  - Features:
    - A form with:
      - Input field for task descriptions.
      - Submit button to add tasks.
    - Section displaying tasks dynamically as an unordered list.

#### **Testing Requirements**
- Unit tests for:
  - `add_task(task)` – Verifies tasks are added correctly.
  - `get_tasks()` – Validates tasks are retrieved accurately.
- Use the `unittest` module for all test cases.

---

### **Example Input/Output**

#### **Adding Tasks**
1. **Input:**  
   Task: Buy groceries
2. **Output:**  

#### **Adding Another Task**
1. **Input:**  
Task: Clean the house
2. **Output:**  

#### **Testing**
- Test cases validate:
- Tasks are added as expected.
- Tasks are retrieved correctly.

---

## **Getting Started**

### **Dependencies**
- Python 3.10+
- Flask
- Unittest module

### **Run the Application**
1. Clone the repository:
```bash
git clone https://github.com/raneem-tamer/To-Do-List-Requirements.git
