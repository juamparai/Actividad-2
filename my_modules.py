def generate_structure (names, stat1, stat2, stat3):
    """ This function zips four different lists into one making a list of uppered names from the first list, which has to be a string"""
    names_uppered = names.upper ()
    names_list = names_uppered.split(', ')
    zipped_file = zip (names_list, stat1, stat2, stat3)
    zipped_file_list =  list (zipped_file)
    return (zipped_file_list)

def calculate_top (team_data, stat_number):
    """ This function recieves the calculates: 
        The topscorer if entered 1
        The player who avoided more goals if entered 2
        The top assist if entered 3 """
    max_stat = max(team_data, key=lambda x: x[stat_number])
    return (max_stat)

#def calculate_best (team_data):
    """ This function returns the best player according to a weighted mean
        Goal as 1.5, avoided goal as 1.25 and assist as 1 """
    