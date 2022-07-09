import time
import random


def print_wait(msg):
    print(msg)
    time.sleep(2)


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_wait(f'Sorry, the option "{option}" is invalid. '
                   'Try again!')


def play_again():
    print_wait("Would you like to play again? Enter y or n")
    play = valid_input("Enter y or n", ["y", "n"])
    if play == "y":
        print_wait("Loading game...")
        game()
    elif play == "n":
        print_wait("Thanks for playing!")
    else:
        play_again()


def chapter1():

    print_wait("You find yourself standing in an open field, "
               "filled with grass and tall weeds.")

    print_wait("Rumor has it that a "
               " strange cult is headquartered somewhere "
               "around town and "
               "people have been disappearing.")
    print_wait("In front of you is a castle.")
    print_wait("To your right is a forest.")
    print_wait("In your hand you hold a rusty dagger.")


def field(weapon, character):
    print_wait("Enter 1 to knock on the castle door.")
    print_wait("Enter 2 to go into the forest.")
    print_wait("What would you like to do?")
    while True:
        option1 = valid_input("Please enter 1 or 2.", ["1", "2"])
        if option1 == "1":
            house(weapon, character)
            break
        elif option1 == "2":
            forest(weapon, character)
            break


def house(weapon, character):
    print_wait("A strange " + character +
               " answers the door and invites "
               "you inside and you walk in.")
    print_wait("The " + character + " asks you to sit "
               "down while they use the restroom.")
    print_wait("You hear a faint sound and you get up to "
               "approach the sound in the connecting room. ")
    print_wait("You discover a radio in a room "
               "full of weird looking symbols.")
    print_wait("The " + character + " returns with a knife "
               "in hand and a menacing "
               "glare as they approach you.")
    if "dynamite" not in weapon:
        print_wait("You feel extremely fearful "
                   " only having a rusty dagger. ")
    print_wait("Enter 1 to dive through the open window to escape to the field.")
    print_wait("Enter 2 to fight.")
    print_wait("What would you like to do?")   
    while True:
        option2 = valid_input("Enter 1 or 2 ", ["1", "2"])

        if option2 == "2":
            if "dynamite" in weapon:
                print_wait("you light the dynamite, throw it "
                           "at the " + character +
                           ", and dive out of the window")
                print_wait("The house blows up as you run away")
                print_wait("Congratulations, you have "
                           "survived and defeated the cult member.")
            else:
                print_wait("You fight the " + character +
                           " with your rusty "
                           "dagger and and get knocked out "
                           "from behind by someone.")
                print_wait("You have lost.")
            play_again()
            break

        if option2 == "1":
            print_wait("You dive out of the "
                       "window and run back to the field")
            field(weapon, character)
            break


def forest(weapon, character):
    if "dynamite" in weapon:
        print_wait("You walk cautiously into the forest.")
        print_wait(" You have already removed the dynamite")
        print_wait("You go back to the field. ")
    else:
        print_wait("You walk cautiously into the forest.")
        print_wait("There is a dripping "
                   "sound echoing nearby.")
        print_wait("As you approach the dripping sound, "
                   "you find a stick of dynamite "
                   "and pick it up.")
        print_wait("You throw away your rusty dagger "
                   "and walk back to the field.")
        weapon.append("dynamite")
    field(weapon, character)


def game():
    weapon = []
    character = random.choice(["strange man", "sketchy woman",
                               "Grandma", "Grandpa"])

    chapter1()
    field(weapon, character)


game()
