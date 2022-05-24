import json

# try:
with open('test.json', 'r') as f:
    x = json.load(f)
# except FileNotFoundError:
#     username = 'x'
#     with open('test.json', 'w') as f:
#         json.dump(username, f)