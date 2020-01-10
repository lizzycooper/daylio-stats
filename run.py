import csv
import datetime
from entry import daylio_entry

# All entries will be in this list
entries_list = []

# Daylio export is in file location
with open('./daylio_export10jan2020.csv', newline='') as csv_file:
    data = csv.reader(csv_file, delimiter=',', quotechar='"')

    # Create a daylio_entry instance for each row in the CSV, have them all in a list
    for row in data:
        if row[1] == 'date':
            pass
        else:
            entries_list.append(daylio_entry(row))

def define_date_range():
    print('What is the date range you would like to analyse? If you would like to analyse a whole year, enter the year.')
    year_choice = input('If you would like to analyse a custom date range, just enter \'other\' now: ')

    # Removes entries not in the given year
    if year_choice >= '2010' and year_choice <= '2040':

        for entry in entries_list:
            if entry.matches_year == False:
                entries_list.remove(entry)
    
    # Removes entries not in the given date range
    elif year_choice == 'other':

        min_date = input('Enter the first date you would like to analyse, in the format \'YYYY-MM-DD\': ')
        max_date = input('Enter the first date you would like to analyse, in the format \'YYYY-MM-DD\': ')