# Get user to enter all the moods in order for analysis
def create_moods():
    moods_dict = {}
    
    print('Enter each mood you have configured in Daylio, taking care to go from WORST MOOD (ie. "depressed", "awful") to BEST MOOD (ie. "rad", "great"). Ensure not to make any spelling errors. Press Enter after each mood, and after entering all moods just press Enter again.')
    
    # Creates a dictionary of moods with numbers assigned e.g. {'sad': 1, 'happy': 2}
    i = 1
    current_mood = input('Enter mood ' + str(i) + ': ')

    while current_mood != '':
        i += 1
        moods_dict[current_mood] = i
        current_mood = input('Enter mood ' + str(i) + ': ')
    
    return moods_dict