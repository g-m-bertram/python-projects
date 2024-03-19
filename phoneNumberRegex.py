"""
basic regular expression (regex) program to find a phone number in a string

1. import re
2. create regex object with re.compile() (use raw string)
3. pass the string you want to search into search() method
    returns a match object
4. call the match object's group() method to return a string of the matched text
"""

import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo.group(1))
print(mo.group(2))

# return entire matched text
print(mo.group(0))
print(mo.group())

# return all groups
print(mo.groups())

# can assign groups to variables
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

# create slightly different regex which looks for area code in parentheses
phoneNumRegex2 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo2 = phoneNumRegex2.search('My number is (415) 555-4242')
print(mo2.group(1))
print(mo2.group(2))