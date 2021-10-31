#################################################################
# FILE : helper.py
# WRITER : Chen Scheim , chenscheim , 316539949
# EXERCISE : intro2cs2 ex9 2021
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED: -
# NOTES: -
#################################################################
import json

def load_json(filename):
    json_file = filename
    with open(json_file, 'r') as file:
        car_config = json.load(file)
    # now car_config is a dictionary equivalent to the JSON file
    return car_config
