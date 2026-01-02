import random
import time

# -----------------------------
# Game State
# -----------------------------
moves_left = 6
inventory = []
game_over = False

# -----------------------------
# Helper Functions
# -----------------------------


def show_status():
    print("\n----------------------------")
    print(f"Moves left: {moves_left}")
    print(f"Inventory: {inventory if inventory else 'Empty'}")
    print("----------------------------\n")


def show_objective():
    print("\nOBECTIVE:")
    print("Uncover whether the secret student organization is malicious.")
    print("Collect enough evidence (documents, photos, recordings)")
    print("before time runs out.")
    print("You need at least TWO strong pieces of evidence")
    print("before confronting the organization.")
    print("Choose wisely. Some actions waste time.\n")


def random_event():
    global moves_left
    event = random.choice(["nothing", "delay", "tip"])

    if event == "delay":
        print("Random Event: Campus lockdown delays your investigation.")
        moves_left -= 1
    elif event == "tip":
        print("Random Event: An anonymous student gives you a useful tip.")
        if "documents" not in inventory:
            inventory.append("documents")
            print("You obtained: documents")
    else:
        print("Nothing unusual happens.")


def investigate_library():
    print("You search restricted archives in the library.")
    if "documents" not in inventory:
        inventory.append("documents")
        print("You found confidential documents.")
    else:
        print("You've already collected documents here.")


def investigate_student_center():
    print("You secretly photograph a closed-door meeting.")
    if "photos" not in inventory:
        inventory.append("photos")
        print("You captured suspicious photos.")
    else:
        print("You've already taken photos here.")


def follow_member():
    print("You follow a member to a restricted building.")
    if "recordings" not in inventory:
        inventory.append("recordings")
        print("You recorded an incriminating conversation.")
    else:
        print("You already have recordings.")


def confrontation():
    print("\nYou confront the organization leaders.")
    if len(inventory) >= 2:
        print("You present your evidence:")
        for item in inventory:
            print(f"- {item}")
        print("\nAdministration launches an investigation.")
        print("The organization is exposed as malicious.")
        print("YOU WIN.")
    else:
        print("You lack solid evidence.")
        print("They deny everything and discredit you.")
        print("GAME OVER.")
    return True


def cinematic_print(text, delay=0.04):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def opening_scene():
    print("\n==============================")
    print("      THE QUIET SOCIETY       ")
    print("==============================\n")

    cinematic_print("Campus was never truly quiet.")
    time.sleep(0.8)

    cinematic_print("Not at night.")
    time.sleep(1)

    cinematic_print("Lights stayed on in buildings no one used anymore.")
    time.sleep(1)

    cinematic_print("Meetings happened behind locked doors.")
    time.sleep(1)

    cinematic_print("And somehow... everyone pretended not to notice.")
    time.sleep(1.2)


# -----------------------------
# Main Game Loop
# -----------------------------
opening_scene()
name = input("Enter your name: ")

print(f"\n{name}, rumors of a secret student organization circulate campus.")
print("Some say they help students. Others say they control things quietly.")
print("Remember trust your instincts.\n")


show_objective()

while moves_left > 0 and not game_over:
    show_status()

    choice = input(
        "Choose an action:\n"
        "1) Investigate Library\n"
        "2) Investigate Student Center\n"
        "3) Follow a Member\n"
        "4) Confront the Organization\n"
        "Enter 1, 2, 3, or 4: "
    )

    moves_left -= 1

    if choice == "1":
        investigate_library()
    elif choice == "2":
        investigate_student_center()
    elif choice == "3":
        follow_member()
    elif choice == "4":
        game_over = confrontation()
        break
    else:
        print("Invalid choice. You lose time hesitating.")

    random_event()

# -----------------------------
# End Game
# -----------------------------
if not game_over:
    print("\nTime has run out.")
    print("The organization continues operating in secrecy.")
    print("FINAL INVENTORY:", inventory)
    print("GAME OVER.")
