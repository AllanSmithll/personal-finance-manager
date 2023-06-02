# Personal Finance Manager

The Personal Finance Manager is a command-line application that helps you manage your personal finances by tracking your planned revenues, planned expenses, saved money, transaction history, debts, and debtors. It provides a set of features to add, remove, and display various financial elements, as well as perform operations like transferring money between files.

## Features

The Personal Finance Manager offers the following features:

1. Display Planned Revenues: View a list of your planned revenues.
2. Add Planned Revenue: Add a new planned revenue to your financial plan.
3. Remove Planned Revenue: Remove a planned revenue from your financial plan.
4. Display Planned Expenses: View a list of your planned expenses.
5. Add Planned Expense: Add a new planned expense to your financial plan.
6. Remove Planned Expense: Remove a planned expense from your financial plan.
7. Display Saved Money: View the amount of money you have saved.
8. Add Saved Money: Add a new entry for money saved.
9. Remove Saved Money: Remove an entry for saved money.
10. Display Transaction History: View a list of your past transactions.
11. Add Transaction: Add a new transaction to your transaction history.
12. Display Debts and Debtors: View a list of your debts and debtors.
13. Add Debt or Debtor: Add a new debt or debtor to your records.
14. Remove Debt or Debtor: Remove a debt or debtor from your records.
15. Update Value by Description: Update the value of a financial element based on its description.
16. Transfer Value between Files: Transfer a certain amount of money from one file to another.
17. Exit: Save changes and exit the program.

## Getting Started

To use the Personal Finance Manager, follow these steps:

1. Clone the repository to your local machine.
2. Make sure you have Python 3 installed.
3. Run the main.py file to start the application:

`python main.py` or `python3 main.py`

5. Follow the on-screen instructions to navigate and use the Personal Finance Manager.

## Usage

When you run the application, you will be presented with a menu displaying various options. Simply enter the number corresponding to the action you want to perform and follow the prompts.

For example, to add a planned expense, you would choose option 5, enter the description of the expense, its value, and whether it is approved or not. The application will then add the expense to your financial plan.

Make sure to save your changes by selecting the "Exit" option before closing the application.

## File Structure

The project has the following file structure:

- 📦Personal-Finance-Manager
- ┣ 📂classes
- ┃ ┣ 📜fileMethods.py
- ┃ ┗ 📜FinancesManager.py
- ┣ 📂data
- ┃ ┣ 📜debtors-debts.csv
- ┃ ┣ 📜historic.csv
- ┃ ┣ 📜planned_expenses.csv
- ┃ ┣ 📜planned_revenues.csv
- ┃ ┣ 📜saved_money.csv
- ┃ ┗ 📜summation.txt
- ┣ 📜.gitignore
- ┗ 📜main.py

- The `classes` directory contains the `FinancesManager` class, which handles the financial operations.
- The `data` directory stores the text files used to store the financial data, such as planned expenses, revenues, saved money, historic, and debtors.
- The `main.py` file is the entry point of the application.
- The `README.md` file provides information about the project.

## Contributing

Contributions to the Personal Finance Manager are welcome! If you find any issues or have suggestions for improvements, please create a new issue or submit a pull request.

When contributing, please ensure that your code follows the existing coding style and that you include appropriate test cases.

## License

The Personal Finance Manager is open-source software licensed under the MIT license. Feel free to use, modify, and distribute it as per the terms of the license.

## Acknowledgments

The Personal Finance Manager was developed using Python and the principles of object-oriented programming. It makes use of file I/O to store and retrieve financial data.

## Contact

If you have any questions or inquiries, please contact [Allan Amâncio] at [contato.allanamancio@gmail.com].
