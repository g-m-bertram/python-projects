# simple program that tracks mouse position on screen in real time

import pyautogui

print('Press Ctrl-C to quit')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + '  Y: ' + str(y).rjust(4)
        pixelColor = pyautogui.screenshot().getpixel((x,y))
        positionStr += '  RGB: (' + str(pixelColor[0]).rjust(3)
        positionStr += ', ' + str(pixelColor[1]).rjust(3)
        positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
        print(positionStr, end='')
        # end='' prevents newline char from being added to the end
        print('\b' * len(positionStr), end='', flush = True)
        # \b erases a char at the end of the current line
        # erases all chars in positionStr
        # flush=True used to ensure screen updates correctly with \b
        
except KeyboardInterrupt:
    print('\nDone')