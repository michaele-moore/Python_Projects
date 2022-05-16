import time
import random
fightlist = [
    "\nYou WIN making it back to the safety of your ship.",
    "\nYou LOSE. Hopefully your crew will tell your story.RIP Captain."]
runlist = [
    "\nYou make it safely aboard. You WIN!",
    "\nYou fall before making it to your ship. You LOSE.Farewell Captain."]
specimenlist = [
    "\nYou grab an empty specimen bag to capture the creature. He gets away!",
    "\nYou grab an empty speciman bag and capture it. Great job Captain!"]
cameralist = [
    "\nHe swims away before you can get the shot.",
    "\nYou snap a clear shot of the creature swimming. Great work Captian!"]


def print_pause(message, delay=1):
    print(message)
    time.sleep(2)


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause('Sorry,that is invalid. Please try again Captain.')


def display_name():
    print_pause("Mission Space-USS Maverick")
    print_pause("\nWelcome Captain!")


display_name()


def story():
    print_pause("\nThe year is 3044.")
    print_pause(
        "Mankind has been set adrfit in space in search of other lifeforms.")
    print_pause(
        "The oldest of these ships is yours to command: the USS Maverick.")
    valid_input("Press 1 to take your seat in the captain's chair.", ['1'])
    print_pause(
        "You navigate to an unexplored planet.")
    print_pause(
        "Please select what eqipment you will take.")


story()


def equip():
    choice = valid_input(
        "\nWill you take SPECIMEN BAGS(1) or CAMERA(2)?", ['1', '2'])
    if choice == '1':
        print_pause("\nYou are now equipped with SPECIMEN BAGS.")
        print_pause(
            "You set out to explore the terrain and vegetation.")
        print_pause(
            "You notice a creature swimming in a stream nearby!")
        valid_input(
            "\nPress 1 to capture the creature in your SPECIMEN BAGS!", ['1'])
        print_pause(random.choice(specimenlist))
    else:
        print_pause("\nYou are now equipped with a CAMERA.")
        print_pause(
            "You set out to explore the terrain and vegetation.")
        print_pause(
            "You notice a creature swimming in a stream nearby!")
        valid_input("\nPress 2 to capture a photo of the creature.", ['2'])
        print_pause(random.choice(cameralist))


equip()


def explore():
    print_pause("Suddenly, you hear rustling in the grass behind you.")
    print_pause("You turn to see an Alien!")
    choice = valid_input(
        "\nWill you stand your FIGHT(1) or RUN(2)?", ['1', '2'])
    if choice == "1":
        print_pause("\nYou decide to fight the Alien!")
        print_pause(random.choice(fightlist))
    else:
        print_pause(
            "\nYou run as fast as you can towards your ship!")
        print_pause(random.choice(runlist))
    print_pause("GAME OVER")


explore()


def replay():
    again = valid_input("\nWould you like to play again? Type 1:>", ['1'])
    if again == "1":
        display_name()
        story()
        equip()
        explore()
        replay()
        return
    else:
        print("Thanks for playing!")
        exit(0)


replay()
