# check users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please type yes or no")


# Main routine
while True:
    want_instructions = yes_no("Would you like to see the instructions ")
    print(f"You chose {want_instructions}")
