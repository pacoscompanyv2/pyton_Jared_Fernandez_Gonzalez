# 1. segundo elemento de la lista
def select_second(L):
    if len(L) < 2:
        return None
    return L[1]

# 2. capitan del peor equipo
def losing_team_captain(teams):
    return teams[-1][1]

# 3. purple shell: intercambia primero y ultimo
def purple_shell(racers):
    racers[0], racers[-1] = racers[-1], racers[0]

# 4. longitudes predichas
lengths = [3, 2, 0, 2]

# 5. fashionably late
def fashionably_late(arrivals, name):
    return name in arrivals[(len(arrivals) + 1) // 2:-1]

if __name__ == "__main__":
    print(select_second([1, 2, 3]))
    print(losing_team_captain([["a", "b"], ["c", "d"]]))

    racers = ["uno", "dos", "tres"]
    purple_shell(racers)
    print(racers)

    print(lengths)

    party_attendees = ["Adela", "Fleda", "Owen", "May", "Mona", "Gilbert", "Ford"]
    print(fashionably_late(party_attendees, "Mona"))
