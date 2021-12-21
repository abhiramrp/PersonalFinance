
# Personal Finance

#### by Abhiram Rishi Pratitpati 


'Personal Finance' is a project where people can manage and track their expenses. It is hard to keep track of checking, credit card, etc. and this application can help users with that. 

## Distinctiveness and Complexity

This project is distinct from previous CS50 projects because it it not a social media website or trading website. Users in this application are prevented from looking at other users' data and are not 
purchasing anything. Users do not have contact with other users and their data is private

This project has 3 models - `User`, `Account`, and `Transaction` with it's own functions that enables automatic updates on fields without writing it on `views.py` or any other file. 
The models have are related through Many-To-One relationships. This is the backend. 

On the front end, there are two files - `inbox.js` and `graphs.js`. The first file helps with deletion of any transactions and it uses AJAX and jQuery. The second file uses `charts.js` and `d3.js` to draw pie charts on the website. 

This project is mobile-responsive. `Bootstrap` is implemented in this website to make it mobile friendly and also aids in CSS. 

Thus, this project satifies the distinctiveness and complexity needed for this course. 

## Files
- [capstone](capstone)
    - [__pycache__](capstone/__pycache__): Cache
    - [__init__.py](capstone/__init__.py): empty
    - [asgi.py](capstone/asgi.py): unites directory apps
    - [settings.py](capstone/settings.py): contains the necessary functions, packages, etc. needed to run the backend
    - [urls.py](urls.py): Connects the admin urls and applicatin urls
    - [wsgi.py](capstone/wsgi.py): unites directory apps
- [finances](finances)
    - [__pycache__](capstone/__pycache__): Cache
    - [migrations](finances/migrations): Has the migrations for every changes made to the database
    - [static/finances](finances/static/finances)
        - [graphs.js](finances/static/finances/graphs.js): Uses `d3.js` for colors and `charts.js` to make pie charts and display the data on the webpage. Source file in [layout.html](finances/templates/finances/layout.html) header. 
        - [index.js](finances/static/finances/index.js): Deletes a transaction using AJAX and jQuery. Source file in [layouts.html] header. 
        - [styles.css](finances/static/finances/styles.css): Has CSS information fields for some of the webpage elements and classes. 
    - [templates/finances](finances/templates/finances)
        - [account.html](finances/templates/finances/account.html): Displays the purchases from that account. Includes 2 pie charts to display income and expenses. Has the table from [transactions.html](finances/templates/finances/transactions.html)
        - [add_account.html](finances/templates/finances/add_account.html): Add an account
        - [add_transaction.html](finances/templates/finances/add_transaction.html): Adds a transaction
        - [all_transactions.html](finances/templates/finances/all_transactions.html): Displays all the transactions using [transactions.html](finances/templates/finances/transactions.html)]
        - [category.html](finances/templates/finances/category.html): Displays all the transactions from a category (food, gas, etc.) using [transactions.html](finances/templates/finances/transactions.html)]
        - [index.html](finances/templates/finances/index.html): Home page. If not logged in, shows the home page. If logged in, displays the overview of expenses, income, etc. 
        - [layout.html](finances/templates/finances/layout.html): Backbone of all the templates. Includes the files from `charts.js`, AJAX, jQuery, `d3.js`, etc. in the header. 
        - [login.html](finances/templates/finances/login.html): Login form to sign in the web application. 
        - [register.html](finances/templates/finances/register.html): Register form to create an account
        - [transactions.html](finances/templates/finances/transactions.html): Displays the transactions on the page in a table with name, price, etc. 
    - [__init__.py](capstone/__init__.py): empty
    - [admin.py](finances/admin.py): responsible for admin controls on users and thier objects. 
    - [apps.py](finances/apps.py): Configures `Finances` app
    - [forms.py](finances/forms.py): Creates the forms from Model objects
    - [models.py](finances/models.py): Defines the Model classes. 
    - [tests.py](finances/tests.py): Tests models and other functions
    - [urls.py](finances/urls.py): Has url_routes and connects HTML templates to routes in [views.py](finances/views.py)
    - [utils.py](finances/utils.py): Defines any helpful functions thas makes programming easier
    - [views.py](finances/views.py): File that has the routes and completes them with paraemeters, requests, etc. 
    - [db.sqlite3](db.sqlite3): The database where all the information will be stored
    - [manage.py](manage.py): Main file. Rnns the application. 
    - [READMe.md](READMe.md): You are reading me right now


## How to run
1. Go to the directory of this project in the command line. 
2. Run `python3 manage.py runserver`


# Additional Info
This project didn't install any additional files or packages. For the Javascript and CSS operations, Bootstrap and other programs are in the header of layout.html](finances/templates/finances/layout.html)





