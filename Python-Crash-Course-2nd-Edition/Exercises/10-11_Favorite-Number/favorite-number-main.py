import json

filename = 'favorite_numbers.json'


def load_favorite_num():
    """Get favorite number from file if available.
    Otherwise return None.
    """
    try:
        with open(filename) as f:
            fav_num = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_num


def get_new_favorite_num():
    """Get new favorite number from user."""
    fav_num = input("What's your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(fav_num, f)
    return fav_num


def report_favorite_num():
    """Report favorite number from favorite_numbers.json.
    If it doesn't exist, call get_new_favorite_num() function to ask
    user to enter one. If it exists, call load_favorite_num() function
    to simply print it.
    """
    fav_num = load_favorite_num()
    if fav_num:
        print(f"I know your favorite number is {fav_num}.")
    else:
        fav_num = get_new_favorite_num()
        print(f"Ok, I remember your favorite number: {fav_num}.")


report_favorite_num()