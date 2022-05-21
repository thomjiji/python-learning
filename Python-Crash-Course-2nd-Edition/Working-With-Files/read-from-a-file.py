filename = 'plain-file/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()  # readlines() method returns a list

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))