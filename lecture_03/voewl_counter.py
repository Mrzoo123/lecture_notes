def main():
    name = input("Name: ").lower()
    number_of_vowels = 0

    for i in range(len(name)):
        if name[i] == "a" or name[i] == "e" or name[i] == "i" or name[i] == "o" or name[i] == "u":
            number_of_vowels += 1

    print("Out of {} letters, {} has {} vowels.".format(len(name), name.title(), number_of_vowels))


main()
