
from get_data import get_data

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    results = data['results']
    return len(results)
data = get_data('randomuser_data.json')

    