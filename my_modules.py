def generate_structure (names, stat1, stat2, stat3):
    """ This function zips four different lists in one making a list of uppered names from the first list, which has to be a string"""
    names_uppered = names.upper ()
    names_list = names_uppered.split(', ')
    zipped_file = zip (names_list, stat1, stat2, stat3)
    return (zipped_file)

