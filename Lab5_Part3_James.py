Sum = 0
kg=int(input("enter a number (negative to stop): "))


while kg > 0:
    Sum += kg
    kg=int(input("enter another number (negative to stop): "))
    
else:
    print(f'Sum of the entered numbers: {Sum}')

