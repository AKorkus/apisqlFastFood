How to run?
In directory PROJEKT you have to launch app.py.


Files:

app.py - main app to run.
config.py - configuration.

MexicanFastFood.db - data base for menu.
initiator.py - creates database, table "meals" and fills with initial values.
inputs.py - attributes for a table for initiator.py.
meals.json - initial values for a table for initiator.py
json_handler.py - functions for reading and processing jsons and text.

views.py - structure of a webpage.
forms.py - forms in the web page to post data.
models.py - for modification of the database from web page / api level.
templates - htmls.
static - style.css.

sql_kommands.py - functions writing sql code from set variables.
sql_executor.py - functions executing sql code.


Config:
initiate_yes_no set to true will create a database in case the old one is deleted.
secret_code - code for app.
meals attr - contains attributes for a meals table.
