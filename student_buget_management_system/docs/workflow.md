# System Workflow

## 1. Workflow Overview

The Student Expense & Budget Management System follows a menu-driven workflow.

The user interacts with the application through the main menu. Based on the selected option, `main.py` calls the appropriate module to perform the requested operation.

---

## 2. Application Startup

When the application starts:

```text id="h0x2lq"
Start
  |
  v
Load transaction data
  |
  v
Display main menu
  |
  v
Wait for user choice
```

The application loads existing transaction records from:

```text
data/expenses.csv
```

If the file does not exist, the application starts with an empty transaction list.

---

## 3. Main Menu Workflow

The main menu provides the following operations:

```text id="d3x7ke"
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

After completing an operation, the application returns to the main menu unless the user chooses Exit.

---

## 4. Add Transaction Workflow

The Add Income and Add Expense operations follow the same basic workflow.

```text id="r2v8da"
Select Add Income / Add Expense
          |
          v
       Enter Date
          |
          v
    Validate Date
       /       \
    Invalid    Valid
      |          |
      |          v
      +------> Enter Category
                    |
                    v
             Validate Category
                /        \
             Invalid     Valid
               |           |
               |           v
               +------> Enter Amount
                             |
                             v
                       Validate Amount
                         /         \
                      Invalid      Valid
                        |            |
                        |            v
                        +------> Enter Description
                                      |
                                      v
                               Validate Description
                                  /          \
                               Invalid       Valid
                                 |             |
                                 |             v
                                 +------> Generate ID
                                               |
                                               v
                                      Create Transaction
                                               |
                                               v
                                      Add to Transaction List
                                               |
                                               v
                                           Confirmation
```

---

## 5. View Transactions Workflow

```text id="q7f4cy"
Select View Transactions
          |
          v
Check Transaction List
      /          \
   Empty        Contains Data
     |               |
     v               v
"No Transactions"  Display Records
```

Each transaction displays:

- ID
- Date
- Type
- Category
- Amount
- Description

---

## 6. Search Workflow

The user can search by:

- Date
- Category
- Transaction type

Workflow:

```text id="7qmb2v"
Select Search
      |
      v
Choose Search Type
      |
      v
Enter Search Value
      |
      v
Compare With Transactions
      |
      v
Matching Transactions?
     /          \
   No            Yes
   |              |
   v              v
"No Match"    Display Results
```

---

## 7. Edit Workflow

```text id="4zy7qk"
Select Edit Transaction
          |
          v
Enter Transaction ID
          |
          v
Find Transaction
       /       \
    Not Found  Found
       |          |
       v          v
Display Error   Select Field
                   |
                   v
             Enter New Value
                   |
                   v
                Validate
               /        \
           Invalid      Valid
              |           |
              v           v
          Error Message  Update
                            |
                            v
                      Confirmation
```

---

## 8. Delete Workflow

```text id="9n2x3a"
Select Delete Transaction
          |
          v
Enter Transaction ID
          |
          v
Find Transaction
       /       \
    Not Found  Found
       |          |
       v          v
Display Error   Remove Transaction
                   |
                   v
               Confirmation
```

---

## 9. Budget Workflow

The user first sets a monthly budget.

```text id="v7r5sa"
Set Monthly Budget
       |
       v
Enter Budget
       |
       v
Validate Budget
       |
       v
Store Budget
```

When the user views the budget status, the system calculates:

```text id="9w1w0x"
Monthly Budget
      |
      +----> Total Expenses
      |
      v
Remaining Budget
      |
      v
Budget Usage Percentage
      |
      v
Budget Status
```

The system can display:

- Monthly budget
- Total expenses
- Remaining budget
- Budget used percentage
- Budget status

---

## 10. Financial Analysis Workflow

```text id="j9k2qa"
Select Financial Analysis
          |
          v
Read Transactions
          |
          +----> Calculate Total Income
          |
          +----> Calculate Total Expenses
          |
          +----> Calculate Net Savings
          |
          +----> Calculate Savings Percentage
          |
          +----> Calculate Category Totals
          |
          +----> Find Highest Expense
          |
          +----> Find Lowest Expense
          |
          +----> Find Highest Spending Category
          |
          v
Display Financial Analysis
```

---

## 11. Financial Report Workflow

The financial report combines the results of the analysis and budget modules.

```text id="m1x7ec"
Select Generate Report
          |
          v
Read Transactions
          |
          +----> Financial Calculations
          |
          +----> Budget Calculations
          |
          +----> Category Analysis
          |
          v
Generate Formatted Report
          |
          v
Display Report
```

The report includes:

- Total income
- Total expenses
- Net savings
- Savings percentage
- Monthly budget
- Remaining budget
- Budget usage
- Budget status
- Category-wise expenses
- Highest expense
- Lowest expense
- Highest spending category

---

## 12. Save and Load Workflow

### Loading Data

```text id="u4q6py"
Application Starts
       |
       v
Check expenses.csv
    /          \
 Missing       Exists
   |              |
   v              v
Empty List     Read CSV
                  |
                  v
             Convert Records
                  |
                  v
           Transaction List
```

### Saving Data

```text id="b2z6hw"
User Selects Save / Exit
          |
          v
Current Transaction List
          |
          v
file_manager.py
          |
          v
Write CSV File
          |
          v
Confirmation
```

---

## 13. Exit Workflow

```text id="6r3y2d"
Select Exit
    |
    v
Save Transactions
    |
    v
Display Confirmation
    |
    v
Exit Application
```

---

## 14. Overall System Workflow

```text id="8qf5nc"
                    START
                      |
                      v
              Load Transaction Data
                      |
                      v
                 Main Menu
                      |
                      v
              User Selects Option
                      |
       +--------------+--------------+
       |              |              |
       v              v              v
 Transactions      Budget         Analysis
       |              |              |
       +--------------+--------------+
                      |
                      v
                  Reporting
                      |
                      v
                  Save Data
                      |
                      v
               Return to Menu
                      |
                      v
                  Exit?
                 /     \
               No       Yes
               |         |
               +------> Save
                          |
                          v
                         END
```