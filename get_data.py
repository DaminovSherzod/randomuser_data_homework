import json

def get_data(filename:str) -> dict:
    """
    You are given a filename. Read the JSON data from the file and return the dictionary.

    Args:
        filename(str): file name
    Returns:
        dict: JSON data
    """

    x = json.loads(filename)
    return x
f = open('randomuser_data.json')
filename = f.read()