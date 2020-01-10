import datetime

# Will create one instance for each row in the export, or entry in Daylio. There can be multiple entries per day.
class daylio_entry():

    def __init__(self, export_row):
        
        # Date is in the format '2019-12-31'
        self.entry_date = export_row[0]

        # Weekday is in the format 'Tuesday'
        self.weekday = export_row[2]

        # Time is in the format '7:21 pm'
        self.time = export_row[3]

        # Moods are (from worst to best): 'Depressed', 'Not happy', 'Alright', 'Happy', 'Great'
        self.mood = export_row[4]

        # Activities are delimited by " | "
        self.activities = export_row[5].split(' | ')

        # Year is first 4 characters of date
        self.year = self.entry_date[0:4]

    # Determine if the entry is in the selected year (must be a number between 2010 and 2060)
    def matches_year(self, year_given):

        if self.year == year_given:
            return True

        else:
            return False

    # Determines if the entry is within the selected date range (including start and end)
    def in_date_range(self, min_date, max_date):

        if self.entry_date >= min_date and self.entry_date <= max_date:
            return True

        else:
            return False