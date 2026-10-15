
initial_temp = int(input('Enter the initial temperature in degrees Celsius: '))
target_temp = int(input('Enter taget temperature: '))
time=0
initial= initial_temp

while initial_temp>=target_temp:
    initial_temp -= 2
    time += 1
    
print(f'It will take {time} minutes for the material to cool from {initial_temp} to {target_temp}')
