import time
import random
import creatures


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro(s):
    print_pause("You find yourself in an open field"
                " filled with grass and sunflowers!")
    print_pause("Rumor has it that a " + s + " is somewhere around here,"
                " and has been terrifying the nerby village.")
    print_pause("In front of you a house")
    print_pause("To your right is a dark cave")
    print_pause("In your hand you hold your trusty"
                " (but not very effective) dagger.\n")


def valid_input(prompt, options):
    while True:
        choice = input(prompt).lower()
        for option in options:
            if option in choice:
                return choice

        print_pause("Sorry I don't understand")


def options(items, s):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice = valid_input("(Please enter 1 or 2.)", ["1", "2"])
    if "1" in choice:
        option1(items, s)
    elif "2" in choice:
        option2(items, s)
    else:
        valid_input()
        options(items, s)


def option1(items, s):
    print_pause("\nYou approach the door of the house.")
    print_pause("You are about to knock when the door opens"
                " and out steps a " + s + " .")
    print_pause("OHH! This is a " + s + " house!")
    print_pause("The " + s + " attacks you!")
    if "Silver Sword of Gith" not in items:
        print_pause("You feel a bit under-prepared for this,"
                    " what with only having a tiny but trusty dagger.\n")
    house = valid_input("Would you like to (1) fight or (2) run away?\n"
                        "Please enter 1 or 2.", ["1", "2"])
    if "1" in house:
        if "Silver Sword of Gith" in items:
            print_pause("\nAs the " + s + " moves to attack you"
                        " take out your new sword.")
            print_pause("The Silver Sword of Gith shines brightly in your hand"
                        " as you brace yourself for the attack.")
            print_pause("But the " + s + " take one look at your shiny new toy"
                        " and runs away!")
            print_pause("You have rid the town of the " + s + "."
                        " You are victorious!")
        else:
            print_pause("\nYou do your best....")
            print_pause("but your dagger is no match for the " + s + ".")
            print_pause("You have been defeated!\n")
    elif "2" in house:
        print_pause("\nYou run back into the field."
                    " Luckily, you don't seem to have been followed.\n")
        options(items, s)


def option2(items, s):
    if "Silver Sword of Gith" in items:
        print_pause("\nYou've been here before and gotten all the"
                    " good stuff. It's just an empty cave now.")
        print_pause("You walked back out to the field\n")
        options(items, s)
    else:
        print_pause("\nYou peer cautiously into the cave.")
        print_pause("Your eye chatches a glint of metal behind the rock.")
        print_pause("You have found the magical Silver Sword of Gith ")
        print_pause("You take the sword with you and"
                    "walk back to the field.\n")
        items.append("Silver Sword of Gith")
        options(items, s)


def play_again():
    play_again = valid_input("Would you like to play again?"
                             "'yes' or 'no'", ["yes", "no"]).lower()
    if "no" in play_again:
        print_pause("OK, Goodby!")
    elif "yes" in play_again:
        print_pause("Very good, let's play again!")
        adventure_game()
    else:
        valid_input()


def adventure_game():
    items = []
    s = random.choice(creatures.creature_names)
    intro(s)
    options(items, s)
    play_again()


adventure_game()
