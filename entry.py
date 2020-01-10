import datetime

# Simply converts full month names to numbers
def month_to_num(month):
    return {
        'January' : 1,
        'February' : 2,
        'March' : 3,
        'April' : 4,
        'May' : 5,
        'June' : 6,
        'July' : 7,
        'August' : 8,
        'September' : 9, 
        'October' : 10,
        'November' : 11,
        'December' : 12
    }[month]

# Will create one instance for each row in the export, or entry in Daylio. There can be multiple entries per day.
class daylio_entry():

    def __init__(self, export_row):
        
        # Date is in the format '2019-12-31', convert this to datetime...
        self.entry_date = export_row[0]

        # Year is first 4 characters of date
        self.year = self.entry_date[0:4]

        # Date in month and month (full name) are derived from the same cell
        self.day_of_month, self.month = export_row[1].split(' ')

        # Get month as a number rather than the full name
        self.month_number = month_to_num(self.month)

        # Get week number of the year from the rest of the date
        self.week_number = datetime.date(int(self.year), int(self.month_number), int(self.day_of_month)).isocalendar()[1]

        # Now we have a datetime
        self.full_date = datetime.date(int(self.year), int(self.month_number), int(self.day_of_month))

        # Weekday is in the format 'Tuesday'
        self.weekday = export_row[2]

        # Time is in the format '7:21 pm'
        self.time = export_row[3]

        # Moods are (from worst to best): 'Depressed', 'Not happy', 'Alright', 'Happy', 'Great'
        self.mood = export_row[4]

        # Activities are delimited by " | "
        self.activities = export_row[5].split(' | ')

    # Represent entry with date and mood
    def __repr__(self):

        return self.entry_date + ': ' + self.mood

    # Determine if the entry is in the selected year (must be a number between 2010 and 2060)
    def matches_year(self, year_given):

        if self.year == year_given:
            return True

        else:
            return False

    # Determines if the entry is within the selected date range
    def in_date_range(self, min_date, max_date):

        if self.entry_date >= min_date and self.entry_date <= max_date:
            return True

        else:
            return False

    # Determines if the entry includes the given activity
    def matches_activity(self, activity):

        if activity in self.activities:
            return True
        
        else:
            return False