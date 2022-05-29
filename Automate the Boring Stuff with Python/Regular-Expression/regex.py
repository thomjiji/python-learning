import re

# Create a regex object with the re.compile() function.
phone_number_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

# Call the regex object's search() method, and then return a Match object.
mo = phone_number_regex.search('My number is 415-555-4242.')

# Call the Match object's group() method to return a string of the actual matched text.
print(mo.group(1))