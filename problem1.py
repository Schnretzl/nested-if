# 1. Nested Decisions: The Adventure Game

# Task 1: Code Correction
# Task 2: Setting the Scene
# Task 3: Default Path
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("Climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    torch = input("Do you want to (light a torch) or (proceed in the dark)? ")
    if torch == "light a torch":
        print("Good idea.  Use a torch to light your way.")
    elif torch == "proceed in the dark":
        print("You can't see very well.  Proceed carefully.")
    else:
        pass
else:
    pass