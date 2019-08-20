total_age = 0
number_of_people = 0

age = int(input("Enter the first age. "))
while age >= 0:
    total_age =+ age
    number_of_people += 1
    print("Accepted.")
    age = int(input("Enter the next age. "))

if number_of_people == 0:
    print("Non defined")
average_age = total_age / number_of_people
print(average_age)