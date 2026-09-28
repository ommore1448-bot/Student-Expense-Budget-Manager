# System Architecture

## 1. Architecture Overview

The Student Expense & Budget Management System follows a **modular architecture**.

The application is divided into separate Python modules. Each module performs a specific responsibility, while `main.py` controls the overall application flow.

The main architectural flow is:

```text
User
  |
  v
main.py
  |
  +----------------------+
  |                      |
  v                      v
Expense Manager      Budget Manager
  |                      |
  v                      v
Transactions          Budget Status
  |
  +----------------------+
  |
  v
Analyzer
  |
  v
Financial Analysis
  |
  v
Report
  |
  v
Financial Report

main.py
  |
  v
File Manager
  |
  v
data/expenses.csv
```

---

## 2. Main Components

### main.py

Acts as the main controller of the application.

Responsibilities:

- Display the main menu.
- Accept user choices.
- Control the application workflow.
- Call functions from other modules.
- Load transaction data when the application starts.
- Save transaction data when required.
- Handle application exit.

---

### transaction.py

Handles the basic transaction structure.

Responsibilities:

- Create transaction dictionaries.
- Display transaction information.
- Provide transaction-related helper functions.

A transaction contains:

- ID
- Date
- Type
- Category
- Amount
- Description

---

### expense_manager.py

Handles transaction management operations.

Responsibilities:

- Add transactions.
- View transactions.
- Search transactions.
- Find transactions by ID.
- Edit transactions.
- Delete transactions.

This module works with the transaction list maintained by the main application.

---

### budget_manager.py

Handles budget-related calculations.

Responsibilities:

- Accept a monthly budget.
- Calculate total expenses.
- Calculate remaining budget.
- Calculate budget usage percentage.
- Determine budget status.
- Display budget summary.

Possible budget statuses include:

- Within Budget
- Budget Almost Exceeded
- Budget Exceeded

---

### analyzer.py

Performs financial analysis.

Responsibilities:

- Calculate total income.
- Calculate total expenses.
- Calculate net savings.
- Calculate savings percentage.
- Calculate category-wise expenses.
- Find the highest expense.
- Find the lowest expense.
- Find the highest spending category.

---

### report.py

Generates the consolidated financial report.

Responsibilities:

- Collect calculated financial information from other modules.
- Display income and expense summaries.
- Display savings information.
- Display budget information.
- Display category-wise expenses.
- Display highest and lowest expenses.
- Display the highest spending category.

The report module uses calculations from the analysis and budget modules instead of duplicating those calculations.

---

### validators.py

Handles input validation.

Responsibilities:

- Validate transaction amounts.
- Validate transaction types.
- Validate dates.
- Validate categories.
- Validate descriptions.
- Validate menu choices.

The validation functions help prevent invalid input from causing unexpected program behavior.

---

### file_manager.py

Handles persistent transaction storage.

Responsibilities:

- Save transactions to CSV.
- Load transactions from CSV.
- Create the data directory when necessary.
- Handle missing transaction files.
- Handle invalid CSV records.

Transaction data is stored in:

```text
data/expenses.csv
```

---

### utils.py

Contains reusable helper functions.

Responsibilities:

- Generate transaction IDs.
- Format monetary amounts.
- Display headings and separators.
- Calculate percentages safely.

---

## 3. Data Flow

The basic data flow of the system