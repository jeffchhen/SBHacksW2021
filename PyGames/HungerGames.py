import random

def players():
    playlist = []
    number = input("Enter the amount of players for the game:")
    i = 1
    while i <= int(number):
        player = input("What is player " + str(i) + "'s name?")
        playlist.append(player)
        i = i + 1
    return playlist


def scenario():
    scenarios = []
    scenarios.append("is hit by a wheelchair.")
    scenarios.append("tackles a werewolf.")
    scenarios.append("gets trampled by horses.")
    scenarios.append("escapes a hyena attack.")
    scenarios.append("runs into a tree.")
    scenarios.append("hangs onto a cliff")
    scenarios.append("eats poisonous berries.")
    scenarios.append("builds a fire.")
    scenarios.append("is kicked in the face.")
    scenarios.append("keeps warm.")
    scenarios.append("trips over a pumpkin.")
    scenarios.append("regains health.")
    scenarios.append("gets a sunburn.")
    scenarios.append("drinks a bottle of water.")
    scenarios.append("is ran over by a truck.")
    return scenarios


def rando(rnumbers,participants):
    rnum = random.randint(0, 13)
    rnumbers.append(rnum)
    if len(rnumbers) == participants:
        return(rnumbers)


def simulate(active_players, scenarios, rando, current_round):
    while True:
        next = input("Press enter to display the results of the next round.")
        if next == "":
            print("Results of Round " + str(current_round))
            r = len(active_players)
            j = 0
            for i in rando:
                print(active_players[j] + scenarios[i])
                if i % 2 != 0:
                    active_players.pop(j)
                if j == r:
                    break
                j = j + 1
            print("The survivors after round" + str(current_round) + "are:")
            for i in active_players:
                print(i)
            return (active_players)
        else:
            continue


def main():
    while True:
        print("Welcome to your Hunger Games Simulation")
        next = input("Press enter to start.")
        if next == "":
            round = 1
            attendees = players()  # get players
            situations = scenario()  # gets possible scenarios
            rnumbers = []
            # simulation
            while True:
                if len(attendees) == 1:
                    print("Thanks for playing!")
                    break
                random = rando(rnumbers, attendees)
                simulate(attendees, situations, random, round)
                round = round + 1
        else:
            continue
        break

main()