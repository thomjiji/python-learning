import json

favor_num = input("What's your favorite number? ")

filename = 'favorite_numbers.json'

with open(filename, 'w') as f:
    json.dump(favor_num, f)