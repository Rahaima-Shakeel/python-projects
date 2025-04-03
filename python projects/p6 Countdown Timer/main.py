# Imports the `time` module, takes user input for countdown duration, converts seconds into hours, minutes, and seconds, displays the countdown in HH:MM:SS format, updates every second using `time.sleep(1)`, and shows a "TIME'S UP!" message when the countdown reaches zero.

import time

my_time= int(input("Enter the time in seconds: "))
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    
print ("TIME'S UP!")