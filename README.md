# The Money-Track App: The Income & Expense Tracker App

Welcome to The Money Track App. The objective of the Money-Track App is a simple and user-friendly income and expense tracking app, allowing Users to easily input their income and expenses, categorize their expenses, view their spending history, generate expense reports and delete transactions. The core mechanic of the App is to keep accurate records of the inflow and outflow of money.

![Responsiveness](assets/images/responsive.webp) 

[You can view this app here](https://money-track-0848dea2992f.herokuapp.com/)


## User Stories

### New Users:
- As a new User, I would like to add my income and expenses.
- As a new User, I would like to keep track of my expenses.
- As a new User, I would like the App to be simple and easy to use.
- As a new User, I would like to see all my transactions.
- As a new User, I would like to check my balances.
- As a new User, I would like to be able to delete transactions if I wish to do so.

### Return Users:
- As a return User, I would like to keep track of my monthly income and expenses.


## UX Design
Although this project is primarily a terminal-based application, The Money Track App is designed to provide a user-friendly experience with the following key UX design prinicples taken into consideration:

### Design
<strong>Clear and concise interface:</strong>
- <strong>Menu-driven:</strong> The App utilizes a simple, numbered menu system, making it easy for Users to navigate and select desired actions.
- <strong>Minimalist design:</strong> The interface focuses on essential information, avoiding clutter and distractions.

<strong>User guidance:</strong>
- <strong>Clear instructions:</strong> The App provides clear instructions and prompts at each step, guiding Users through the process of adding, viewing, managing and deleting transactions.
- <strong>Error handling:</strong> The App includes robust error handling mechanisms with informatinve error messages, guiding Users towards correct inputs.

<strong>Visual feedback:</strong>
- <strong>Clear formatting:</strong> Transaction data is presented in a well-organised and easy-to-read format, improving data comprehension.
- <strong>Colorama:</strong> The use of colorama enhances the User experience by providing visual cues through highlighted (color) text. For example, Green for success messsages, Red for errors, and Blue for informational messages.
The color Green is used as it represents growth and prosperity, the color Blue represents trust and the color Red represents a warning signal.

<strong>Data persistence:</strong>
- <strong>Data saving:</strong> The App saves transaction data to a JSON file, ensuring data persistence and allowing Users to continue tracking their finances across sessions.

<strong>User control:</strong>
- <strong>Flexibility:</strong> The App offers Users flexibility in managing their transactions, allowing them to add, view, filter, delete, generate reports, and exit the program.
- <strong>Confirmation:</strong> The App includes confirmation prompts before deleting transactions, ensuring Users are certain about their actions.

These UX design considerations contribute to a more intuitive and enjoyable User experience, making The Money Track App easier to use and more effective for managing personal finances.

### App Flowchart (created on LucidApp):

Before I started building the App, I mapped out the basic structure of the flowchart and I used LucidApp to create the flowchart.

![Flowchart](assets/images/flowchart.jpg)


## How the App works:

##### INITIALIZATION:
- The code imports the neccessary libraries: json, colorama, os and datetime.
- The 'init' function from colorama calls to enable colored text to output in the terminal.
- The 'clear' function defines to clear the terminal screen using os.system for clarity.

##### INTRODUCTION
- The App welcomes the User and introduces itself as The Money Track App that helps the User manage their personal finances.

##### MAIN MENU
- The App presents the User with a menu of options:
    1. Add income or expense
    2. View transactions
    3. Check balance
    4. View transactions by category
    5. Generate monthly report
    6. Delete a transaction
    7. Exit

![App Terminal](assets/images/01-welcome-menu-screen.png)

##### USER CHOICE
The App will perform the action which the User has selected:
- Add income or expense (Option 1)
    - The App will ask the User to specify whether they want to add "income" or "expense".
    - The User can then enter the category of the transaction '(e.g., "Salary", "Bonus")'.
    - The User will be prompted to enter the amount of the transaction.
    - The App will confirm the details and add the transaction to their records.

![App Terminal](assets/images/02-transaction-menu-select-option01.png)

-----

- Add income or expense (Option 2)
    - The App will ask the User to specify whether they want to add "income" or "expense".
    - The User can then enter the category of the transaction '(e.g., "Rent", "Food", "Transport", "Utilities", "Miscellanous")'.
    - The User will be prompted to enter the amount of the transaction.
    - The App will confirm the details and add the transaction to their records.

![App Terminal](assets/images/02-transaction-menu-select-option02.png)

-----

##### RETURN TO 'MAIN MENU'
- The User can return to the 'Main Menu' by typing 'back'.

![App Terminal](assets/images/03-return-main-menu-screen.png)

-----

- View transactions (Option 2)

    - This option will display a list of all their recorded transactions, including the type (income/expense), category, and amount.

![App Terminal](assets/images/09-view-transactions-screen.png)

-----

- Check balance (Option 3)
    - The App will calculate and display their current balance, which is the sum of all their income transactions minus the sum of all their expense transactions.

![App Terminal](assets/images/05-check-balance-screen.png)

-----

- View transactions by category (Option 4)
    - The User can view their transactions filtered by a specific category.
    - The App will first display a list of all their recorded transactions.
    - Then, the User will be prompted to enter the category they want to see.
    - The App will then display only the transactions that belong to that category.

![App Terminal](assets/images/05-view-transactions-category-screen.png)

-----

- Generate monthly report (Option 5)
    - This option will generate a report that summarizes their income and expenses for each month.
    - The report will show the total amount of income and expenses for each month.

![App Terminal](assets/images/06-generate-monthly-report.png)

-----

- Delete a transaction (Option 6)
    - The User can delete transactions from their records.
    - The App will first display a list of all their transactions.
    - The User will be prompted to enter the number(s) of the transaction(s) they want to delete.
    - The App will confirm their choice before deleting the transaction(s).

![App Terminal](assets/images/07-delete-transaction-screen.png)

-----

- Exit (Option 7)
    - This option will exit the App.

![App Terminal](assets/images/08-exit-screen.png)

##### SAVING TRANSACTIONS:
- The App saves the Users transaction data in a file named "transactions.json" whenever they add, edit a transaction. This ensures that their data is persistent and doesn't disappear when they close the App.


## Feature overview:

| function name(s) | Description  | Key Features |
| ---------------- |------- | ------------- |
| load_transactions() | The feature loads transactions to a JSON file | Uses try/except to handle file-related errors |
| save_transactions(transactions) | The feature saves the current list of transactions to a JSON file | Ensures data persistence |
| add_transaction(transactions) | The feature allows the User to add a new transaction ("Salary" for income or "Rent" for expenses) | Validates inputs; Promts for transaction type, category and amount; Adds timestamp to each transaction; Highlights errors for invalid inputs |
| view_transactions(transactions) | The feature displays all transactions in tabular format | Uses tabulate to present data in a readable table format; Differentiates between income and expenses using  appropriate labels |
| delete_transaction(transactions) | The feature deletes specific transactions based on User input | Allows selecting multiple transactions for deletion using indices; Validates User input for valid transaction numbers; Asks for confirmation before deletion; Handles invalid confirmation inputs and promts the User again |
| main_menu() | The feature acts as the central menu to navigate the App | Displays options for managing transactions; Handles User input and calls the appropriate function; Loops until the User chooses to quit |


## Testing
- Testing was conducted regularly throughout the development process as well as at the end of the project to ensure functionality and identify any issues.
- Manual input testing was carried out to simulate real-world usage of the application. This involved entering data manually into the terminal system to ensure that all inputs were handled correctly and that the User interface responded appropriately.
- Testing was also done by friends and family to get feedback to improve User experience.
- PEP8 Validator was used regulary to ensure that the code meets all necessary standards and specifications.
- Bugs that were encountered during testing have been documented in the Bug section, detailing the nature of the issue and the solution.

### Bugs (fixed)

| Bug | Description  | Issues | Fixed |
| --- |------------- | ----------------- | -----------|
| SyntaxError | Incorrect operator used to check if integer selection | ![screenshot](assets/images/error-02.png) | ![screenshot](assets/images/error-02-fixed.png) |
| NameError in the add_transaction function | 'description = input' not defined | ![screenshot](assets/images/name-error-03.png) | ![screenshot](assets/images/name-error-03-fixed.png) |
| KeyError in the check_balance function | Incorrect string "formatted_amount" used instead of "amount" | ![screenshot](assets/images/error-04.png) | ![screenshot](assets/images/error-04-fixed.png) |
| KeyError in check_balance function | Incorrect string "formatted_amount" used instead of "amount" | ![screenshot](assets/images/error-04.png) | ![screenshot](assets/images/error-04-fixed.png) |
| NameError in the add_transaction function | The function was incorrectly named as "save_transactions(transaction)" instead of "save_transactions(transactions)" | ![screenshot](assets/images/error-05.png) | ![screenshot](assets/images/error-05-fixed.png) |
| TypeError in view_transactions_by_category function | List indices was a string and not an integer or slice | ![screenshot](assets/images/error-06.png) | ![screenshot](assets/images/error-06-fixed.png) |
| NameError with import os | os.system not correctly called by import request | ![screenshot](assets/images/name-error-error-07.png) | ![screenshot](assets/images/error-07-fixed.png) |
| IndexError in the delete_transaction function | os.system not correctly called by import request | ![screenshot](assets/images/index-error-08.png) | ![screenshot](assets/images/error-08-fixed.png) |
| NameError in the view_transaction function | the try block was not correctly named | ![screenshot](assets/images/name-error-09.png) | ![screenshot](assets/images/error-09-fixed.png) |


## Validation
Validator testing has been done on: [CI Python validator](https://pep8ci.herokuapp.com/)

| File | screenshot | Notes |                                                                                                 |
| --- | --- | --- | ----------------------------------------------------------------------------------------------------------|
| run.py  | ![screenshot](assets/images/pep8.png) |  All clear, no errors found |


## Tools & Technologies used

The main functions are generated with Python.

#### Below is a list of the technologies used:
- phython
- node.js
- Git used for version control (git add, git commit, git push)

#### Below is a list of the tools used:
- GitHub template reused from love sandwiches
- Gitpod used for local IDE for development
- Heroku (deployment)
- GitHub Pages used for hosting the deployed front-end site


## Deployment
The site was deployed to a Heroku page using a GitHub repository for data storage.

### Configure Heroku 
The steps to configure Heroku are as follows:

Log in to your account, or set up a new one

![screenshot](assets/images/heroku-login.png)

Create a new app on Heroku

![screenshot](assets/images/heroku-create-new-app.png) 

#### Add a buildpack

Next, add a Heroku buildpack to your app. 

![screenshot](assets/images/heroku-add-buildpacks.png)

Click add a buildpack to your app and configure it first for Python and then for NodeJS.

![screenshot](assets/images/heroku-buildpacks-py-js.png)

#### Connect to GitHub
Next, you can configure deploys with Github. If you prefer to deploy without using Github, you can read Heroku's deployment ([documentation](https://devcenter.heroku.com/categories/deployment)). 

In the Deploy tab, select the option to Connect this app to GitHub

![screenshot](assets/images/heroku-deploy-connect-github.png)

Select the branch you want to deploy your app from

![screenshot](assets/images/heroku-manual-deploy.png)

### Accessing deployed project from Github:
- In the Github repository, navigate to the right-hand side, click on the Github pages under the Deployments section.
  
- Under the Github-Pages Deployments section, click on the link to the completed website.

- The live link can be found [here:](https://money-track-0848dea2992f.herokuapp.com/)


## Credits

### Code:

| No | Description  | Source | URL |
| -- | ------------ | ------ | --- |
| 1 | If/Else Statements | Video Tutorial; w3schools.com | https://www.youtube.com/watch?v=-BOBedcjySI https://www.w3schools.com/python/python_conditions.asp |
| 2 | Loops | Video Tutorial portal stackoverflow.com | https://www.youtube.com/watch?v=zmIdC0_0BgY. https://stackoverflow.com/questions/69827626/python-program-that-loops-until-the-user-says-no-then-will-sum-all-transactions |
| 3 | Try/Except Blocks | Video Tutorial; python.org/ | https://www.youtube.com/watch?v=tIh42X0oGQc https://wiki.python.org/moin/HandlingExceptions |
| 4 | Input Validation | Video Tutorial; portal stackoverflow.com | https://www.youtube.com/watch?v=LUWyA3m_-r0 https://stackoverflow.com/questions/64669241/how-do-i-validate-a-users-input-and-make-sure-it-is-the-correct-type-and-within |
| 5 | Listing recoded data | portal stackoverflow.com | https://stackoverflow.com/questions/65364473/pandas-sorting-transactions-into-categories |
| 6 | Filtering transactions | Video Tutorial, portal stackoverflow.com | https://www.youtube.com/watch?v=MXQN6nnEwOU https://stackoverflow.com/questions/55562888/applying-filter-functions-on-a-dataframe |
| 7 | Defining Functions in Python | Code Institute: LSM | https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+CPP_06_20+3/courseware/272f493b4d57445fbd634e7ceca3a98c/6327affd7b854149baab0d0fc59a2fcf/ |
| 8 | Calling Functions | Code Institute: LSM | https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+CPP_06_20+3/courseware/272f493b4d57445fbd634e7ceca3a98c/6327affd7b854149baab0d0fc59a2fcf/ |
| 9 | How to use Colorama | Video Tutorial; portal stackoverflow.com | https://www.youtube.com/watch?v=GPBUFMOXI6M https://stackoverflow.com/questions/9846683/how-to-install-colorama-in-python |
| 10 | How to import os | Code Institute: LSM; Video Tutuorial | https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+CPP_06_20+3/courseware/272f493b4d57445fbd634e7ceca3a98c/4ab3e01af44f4bf2828739c1d0591a45/ https://www.youtube.com/watch?v=xQ7caEk8-5I |
| 11 | Lists | Video Tutuorial; freecodecamp.org | https://www.youtube.com/watch?v=tSgWs9JdpAI https://www.youtube.com/watch?v=9OeznAkyQz4 https://www.freecodecamp.org/news/how-to-use-lists-in-python/ |
| 12 | How to break long lines of code | Video Tutuorial; datacamp.com | https://www.youtube.com/watch?v=SzL2Oo3RktU https://www.datacamp.com/tutorial/how-to-line-break-in-python |

### Template

The Python Essentials Template from Code Institute was used to create my Github repository:
https://github.com/Code-Institute-Org/p3-template

### Acknowledgements:
My mentor, Rory Sheridan, for his advice and guidance throughout this project. He also introduced me to colorama for generating color to the terminal messaging as well as a code snippet to clear the terminal to get rid of any code clutter:

    def clear():
        """
        Clear function to clean-up the terminal so things don't get messy.
        """
        os.system("cls" if os.name == "nt" else "clear")

This project contains some commit messages that are longer than the ideal length. This was done to provide more context and clarity for specific changes, especially those involving complex refactorings or bug fixes.

I understand that concise commit messages are generally preferred, and I will strive to improve the conciseness of future commit messages.