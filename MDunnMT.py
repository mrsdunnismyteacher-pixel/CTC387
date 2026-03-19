#MDunn CTC 387 Midterm #11


#Main Program

print("Let's find out if you're lucky :D")
y=11
while (y != 7):
    y = int(input("Enter a number between 0 and 10 "))
    if (y<7):
        print("Your guess is too low. Try again.")
    if (y>7):
        print("Your guess is too high. Try again.")
    if (y ==7):
        print("Winner, winner, chicken dinner")
    if (y<0) or (y>10):
        print("Your guess is not within the requested range.")
