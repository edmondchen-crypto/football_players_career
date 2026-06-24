# Import the libraries to connect to the database and present the information in tables
from easygui import *
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'football.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    codebox('Here are the stats for the players', 'Here are the results',tabulate(results,headings))
    db.close()
'''Football stats'''
#showing options to choose from
while True:
    msg ="Chooce a query"
    title = "Footballers"
    choices = ["Argentina Players", "Portugal Players", "England Players", "Turyike Players", "France Players", "Brazil Players", "Spain Players", "Over 100 career goals & assists", "Midfielders", "Left Footed Forwards", "Right Footed Forwards", "Top 10 Goal Scorers", "PSG players", "Real Madrid Players", "Chelsea Players", "Arsenal Players", "World Cup Winners", "Under 30 y/o Players", "Exit"]
    choice = choicebox(msg, title, choices)
#making it show the information depending on which option you selected.
    if choice == "Argentina Players":
        print_query('argentina_players')
    elif choice == "Portugal Players":
        print_query('portugal_players')
    elif choice == "England Players":
        print_query("england_players")
    elif choice == "Turyike Players":
        print_query("turyike_players")
    elif choice == "France Players":
        print_query("france_players")
    elif choice == "Brazil Players":
        print_query('brazil_players')
    elif choice == "Midfielders":
        print_query('midfielders')
    elif choice == "Left Footed Forwards":
        print_query('left_foot_forwards')
    elif choice == "Right Footed Forwards":
        print_query('right_foot_ballers')
    elif choice == "Top 10 Goal Scorers":
        print_query('top_10_scorers')
    elif choice == "PSG players":
        print_query('paris_saint-germain')
    elif choice == "Real Madrid Players":
        print_query('real_madrid')
    elif choice == "Chelsea Players":
        print_query('chelsea')
    elif choice == "Arsenal Players":
        print_query('arsenal_players')
    elif choice == "World Cup Winners":
        print_query('world_cups_winners')
    elif choice == 'Under 30 y/o Players':
        print_query("young_players")
    elif choice == "Exit":
        break
    elif choice == None:
        break

