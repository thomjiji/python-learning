import json

filename = 'favorite_numbers.json'

with open(filename) as f:
    fav_num = json.load(f)
    print(f"I know your favorite number! It's {fav_num}.")