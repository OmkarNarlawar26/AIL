def vaccum_agent(location,status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    elif location == "B":
        return "Move Left"

# Environment
rooms = {"A":"Dirty","B":"Dirty"}
location = "A"

while "Dirty" in rooms.values():
    action = vaccum_agent(location,rooms[location])
    print(location,rooms[location],"->",action)

    if action == "Suck":
        rooms[location] = "Clean"
    elif action == "Move Right":
        location = "B"
    else:
        location = "A"
print("Final Environment: ",rooms)