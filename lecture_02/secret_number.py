SECRET_NUMBER = 6

guess = int(input("? "))
while guess != SECRET_NUMBER:
    print("Incorrect.")
    guess = int(input("? "))

print("You guessed correctly! ")