loop_variable = 0

while loop_variable != 1:
    age = int(input("How old are you? "))

    if age >= 18:
        print("You are an adult.")
        loop_variable = 1
    elif age < 0:
        print("Invalid Choice.")
    else:
        print("You are a child.")
        loop_variable = 1

