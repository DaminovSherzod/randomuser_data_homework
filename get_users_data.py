from get_data import get_data

def get_users_data(data:dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
    users = []
    results = data['results']
    for i in results:
        name = i['name']
        # a = name['first'] +' '+ name['last'] +' '+ i['phone']
        users.append({
            "first_name": name['first'],
            "last_name": name['last'],
            "phone_number": i['phone']
        })
    return users    

data = get_data('randomuser_data.json')
print(get_users_data(data))