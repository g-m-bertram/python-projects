# adds Wikipedia bullet points to the start of each line of text on the clipboard
# pyperclip: https://pypi.org/project/pyperclip/

import pyperclip

text = pyperclip.paste()

# separate lines and add stars
lines = text.split('\n')
# loop thru all indices for 'lines' list
for i in range(len(lines)):
    # add star to each string in 'lines'
    lines[i] = '*' + lines[i]
    
text = '\n'.join(lines)
pyperclip.copy(text)