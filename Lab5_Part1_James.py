import time
temperature=int(input("Enter the substance's temperature"))

while temperature >= 100:
    print("The temperature is too hight!!")
    time.sleep(.5)
    print("Turn the thermostat down")
    time.sleep(.5)
    print("wait 5 minutes, Then take the temperature again")
    time.sleep(5)
    temperature=int(input("Enter the substance's temperature"))
else:
    print('The temperature is acceptable.')
    print('Check it again in 15 minutes')

