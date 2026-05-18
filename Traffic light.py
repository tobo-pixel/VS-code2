import time
light = "Green"
while True:
    if light == "Green":
        print("Green light - cars can move!")
        time.sleep(5)
        light = "Yellow"
    elif light == "Yellow": 
        print("Yellow light - slow down!")
        time.sleep(2)
        light = "Red"
    elif light == "Red":
        print("Red light - STOP!")
        time.sleep(5)
        light = "Green"