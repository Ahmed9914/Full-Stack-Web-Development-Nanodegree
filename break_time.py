import webbrowser
import time

flag = 0
while (flag < 3):
    time.sleep(10)
    webbrowser.open('https://www.youtube.com/')
    flag = flag + 1

