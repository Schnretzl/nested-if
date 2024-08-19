# 1. Nested Decisions: The Adventure Game

# Task 1: Code Correction
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("Climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        print("I don't know what you did.")
elif place == "cave":
    print("You find a hidden treasure!")