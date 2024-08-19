# 2. Quick Decisions: The Event Planner

# Task 1: Code Correction
# Task 2: Venue Selection
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
if attendees > 200:
    print("sound system")
if attendees > 300:
    print("projector")
if attendees > 500:
    print("refreshments")
    
    
# Task 3: Catering Choices
vegetarian = input("Do you want vegetarian food? (yes/no): ")
if vegetarian == "yes":
    print("Veggie Delight Caterers")
else:
    print("Gourmet Meals Caterers")