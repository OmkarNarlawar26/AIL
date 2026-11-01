# Design and implement a simple reflex agent for the Vacuum Cleaner world and analyze its rational behavior in a given environment. 

def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"

# Initial environment
location = "A"
room = {
    "A": "Dirty",
    "B": "Dirty"
}

for step in range(1, 5):
    status = room[location]
    action = vacuum_agent(location, status)

    print("Step:", step)
    print("Location:", location)
    print("Status:", status)
    print("Action:", action)

    if action == "Suck":
        room[location] = "Clean"
    elif action == "Right":
        location = "B"
    elif action == "Left":
        location = "A"

    print("Room:", room)
    print()

print("Final Location:", location)
print("Final Room Status:", room)