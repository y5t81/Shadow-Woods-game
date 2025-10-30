print ("Welome to shadow woods!")

choice = input("Do you want to go left or right?")

if choice.lower() == "left":
    print("You discover an old cabin with a glowing door!")

    second = input("Do you ENTER or IGNORE it? ")

    if second.lower() == "enter":
        print("Inside, you see a dusty book on a table.")

        third = input("Do you READ or LEAVE it? ")

        if third.lower() == "read":
            print("The book grants you forbidden knowledge. You escape safely!")
        else:
            print("A shadow rises from the book and consumes you! Game over.")


    else:
        print("You walk away, but something follows you...")
        print("You vanish into the darkness. Game over.")


else:
    print("A tall figure emerges from the trees...")
    print("You are never seen again. Game over.")