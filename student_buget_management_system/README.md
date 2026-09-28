# Student Expense & Budget Management System

## 1. Overview

The **Student Expense & Budget Management System** is a Python-based application designed to help students record, manage, and analyze their income and expenses.

The system allows users to maintain transaction records, set a monthly budget, monitor budget usage, analyze spending, and generate a financial report. It uses a modular structure so that different responsibilities are separated into different Python files.

The project demonstrates fundamental Python programming concepts such as variables, input/output, conditional statements, loops, functions, lists, dictionaries, modules, operators, type conversion, and input validation.

---

## 2. Objectives

The main objectives of the project are:

- To record student income and expenses.
- To organize transactions using categories.
- To allow users to search, edit, and delete transactions.
- To set and monitor a monthly budget.
- To calculate total income, expenses, and savings.
- To analyze category-wise spending.
- To identify the highest and lowest expenses.
- To generate a financial report.
- To validate user input and handle invalid data.
- To store transaction data for future use.

---

## 3. Features

### Transaction Management
- Add income.
- Add expenses.
- View all transactions.
- Search transactions by date, category, or type.
- Edit existing transactions.
- Delete transactions.
- Automatically generate transaction IDs.

### Budget Management
- Set a monthly budget.
- Calculate total expenses.
- Calculate remaining budget.
- Calculate budget usage percentage.
- Display the current budget status.

### Financial Analysis
- Calculate total income.
- Calculate total expenses.
- Calculate net savings.
- Calculate savings percentage.
- Display category-wise expenses.
- Find the highest expense.
- Find the lowest expense.
- Find the highest spending category.

### Financial Report
- Display income and expense summary.
- Display savings information.
- Display budget information.
- Display category-wise expenses.
- Display highest and lowest expenses.
- Display the highest spending category.

### Data Management
- Save transactions to a CSV file.
- Load saved transactions when the application starts.
- Handle missing transaction files.
- Skip invalid transaction records during loading.

### Input Validation
- Validate transaction amounts.
- Validate dates.
- Validate categories.
- Validate descriptions.
- Validate transaction types.
- Handle invalid menu choices and numeric input.

---

## 4. Technologies and Tools

- **Python 3**
- Python standard library
- CSV file handling
- VS Code
- Git and GitHub

No external Python packages are required for the current implementation.

---

## 5. Project Structure

```text
Student-Expense-Budget-Manager/
│
├── main.py
├── transaction.py
├── expense_manager.py
├── budget_manager.py
├── analyzer.py
├── report.py
├── validators.py
├── file_manager.py
├── utils.py
│
├── data/
│   └── expenses.csv
│
├── tests/
│   ├── test_transactions.py
│   ├── test_budget.py
│   └── test_analyzer.py
│
├── docs/
│   ├── architecture.md
│   ├── workflow.md
│   └── diagrams/
│
├── README.md
├── statement.md
├── requirements.txt
└── .gitignore
```

---

## 6. Module Description

| File | Responsibility |
| `main.py` | Controls the main menu and application flow |
| `transaction.py` | Creates and handles transaction structures |
| `expense_manager.py` | Adds, views, searches, edits, and deletes transactions |
| `budget_manager.py` | Handles budget calculations and budget status |
| `analyzer.py` | Performs financial and spending analysis |
| `report.py` | Generates the financial report |
| `validators.py` | Validates user input |
| `file_manager.py` | Saves and loads transaction data |
| `utils.py` | Provides reusable utility functions |

---

## 7. Installation

### Prerequisites

Install **Python 3** on your computer.

Verify the installation using:

```bash
python --version
```

### Clone the Repository

```bash
git clone <your-github-repository-url>
```

Move into the project directory:

```bash
cd Student-Expense-Budget-Manager
```

No additional Python packages are required.

---

## 8. Running the Application

Open a terminal inside the project directory and run:

```bash
python main.py
```

The application will display the main menu.

The available operations are:

```text
1. Add Income
2. Add Expense
3. View Transactions
4. Search Transactions
5. Edit Transaction
6. Delete Transaction
7. Set Monthly Budget
8. View Budget Status
9. Financial Analysis
10. Generate Financial Report
11. Save Data
12. Exit
```

---

## 9. Data Storage

Transaction data is stored in:

```text
data/expenses.csv
```

The CSV file stores the following fields:

- Transaction ID
- Date
- Transaction Type
- Category
- Amount
- Description

The application automatically creates the data directory when necessary.

---

## 10. Testing

The application was tested for its major functional operations, including:

- Adding income.
- Adding expenses.
- Viewing transactions.
- Searching transactions.
- Editing transactions.
- Deleting transactions.
- Setting a monthly budget.
- Viewing budget status.
- Performing financial analysis.
- Generating a financial report.
- Saving transaction data.
- Loading saved data after restarting the application.
- Handling invalid amount input.

The application successfully completed the functional tests performed during development.

---

## 11. Error Handling

The application validates user input before processing it.

Examples include:

- Invalid amounts are rejected.
- Empty categories are rejected.
- Empty descriptions are rejected.
- Invalid dates are rejected.
- Invalid transaction types are rejected.
- Invalid transaction IDs are handled.
- Missing transaction files are handled.
- Invalid CSV records are skipped with a warning.

The objective is to prevent invalid input from causing the application to terminate unexpectedly.

---

## 12. Non-Functional Requirements

### Usability
The application provides a numbered menu and clear prompts so that users can operate the system through the command line.

### Reliability
The system validates input and handles missing or invalid stored records to reduce unexpected failures.

### Maintainability
The application is divided into multiple modules, with each module responsible for a specific part of the system.

### Data Integrity
Transaction information is stored using structured CSV fields and validated before being added to the transaction list.

### Performance
The system uses in-memory lists and dictionaries for transaction processing, which is suitable for the expected size of a student expense record.

### Error Handling
Invalid user input and file-related errors are handled using validation and exception handling.

---

## 13. Limitations

- The current application uses a command-line interface.
- Monthly budget information is maintained during the current application session.
- The system does not connect to real banking or payment services.
- The system does not provide financial advice.
- The system does not use a database.

---

## 14. Future Enhancements

Possible future improvements include:

- Persistent storage of monthly budgets.
- Monthly and weekly financial summaries.
- Exporting reports to additional formats.
- Graphical visualization of spending.
- Additional filtering options.
- More detailed date-based analysis.
- A graphical user interface or web interface.

---

## 15. Conclusion

The Student Expense & Budget Management System provides a structured way for students to record and understand their personal income and expenses.

The project demonstrates the practical use of Python programming fundamentals through modular design, data structures, functions, loops, conditional statements, input validation, file handling, and data analysis.

The modular architecture also makes the system easier to test, maintain, and extend with additional features in the future.