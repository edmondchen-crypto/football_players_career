# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'football.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect('football.db')
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
    print(tabulate(results,headings))
    db.close()


menu_choice = ''
while menu_choice != 'STOP':
    menu_choice = input('type the letter for the information you want to see.\n\n'
    'A: Players with over 100 goal and assists.\n'
    'B: Argentine players.\n'
    'C: Portugese Players.\n' 
    'D: Real Madrid players.\n' 
    'E: PSG players.\n'
    'F: Left foot forwards.\n'
    'G: Under 30 players.\n'
    'H: Top 10 goal scores\n' 
    'I: World Cup winners\n'
    'J: Midfielders\n'
    'K: right footers\n'
    'STOP: to exit\n'
    'What would you like to see? ')
    menu_choice = menu_choice.upper
    if menu_choice == 'A':
        print_query('goal_contribation')
    elif menu_choice == 'B':
        print_query('argentina_players')
    elif menu_choice == 'C':
        print_query('portugal_players')
    elif menu_choice == 'D':
        print_query('real_madrid')
    elif menu_choice == 'E':
        print_query('paris_saint-germain')
    elif menu_choice == 'F':
        print_query('left_foot_forwards')
    elif menu_choice == 'G':
        print_query('young_players')
    elif menu_choice == 'H':
        print_query('top_10_scorers')
    elif menu_choice == 'I':
        print_query('world_cups_winners')
    elif menu_choice == 'J':
        print_query('midfielders')
    elif menu_choice == 'K':
        print_query('right_foot_ballers')