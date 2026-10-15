#get input from user
N=int(input("Enter a positive integer: "))
#using another variable to display the inital input
n=N
#variable for sum to be added too
total=0
#the "keep going" variable
base=1


while base <N:
    total +=N
    N -= 2

print(f"The sum of even numbers from {base} to {n} is {total}")

