import csv
import datetime
from entry import daylio_entry

# All entries will be in this list regardless of date range
all_entries = []

# Daylio export is in file location
with open('./daylio_export10jan2020.csv', newline='') as csv_file:
    data = csv.reader(csv_file, delimiter=',', quotechar='"')

    # Create a daylio_entry instance for each row in the CSV, have them all in a list
    for row in data:
        if row[1] == 'date':
            pass
        else:
            all_entries.append(daylio_entry(row))

# Asks the user how much data to analyse and only returns entries in that range
def define_date_range():
    entries_in_range = []

    while True:
        print('What is the date range you would like to analyse? If you would like to analyse a whole year, enter the year.')
        year_choice = input('Or if you would like to analyse a custom date range, just enter \'other\' now: ')

        # Removes entries not in the given year
        if year_choice >= '2010' and year_choice <= '2040':

            for entry in all_entries:
                if entry.matches_year(year_choice):
                    entries_in_range.append(entry)
            break
        
        # Removes entries not in the given date range
        elif year_choice == 'other':

            min_date = input('Enter the first date you would like to analyse, in the format \'YYYY-MM-DD\': ')
            max_date = input('Enter the last date you would like to analyse, in the format \'YYYY-MM-DD\': ')

            for entry in all_entries:
                if entry.in_date_range(min_date, max_date):
                    entries_in_range.append(entry)

            break
        
        else:
            print('Try again, just entering a year or \'other\'. ')
    
    return entries_in_range

# This list will contain all entries in the given date range
entries_list = define_date_range()

print('done')