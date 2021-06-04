import random
import Team
import Player
import Coach

def name_list_maker(names):
    i = 0
    NameList = []
    while i < len(names):
        new_word = ""
        while names[i] != " ":
            new_word = new_word + names[i]
            i += 1
            if i >= len(names):
                NameList.append(new_word)
                return NameList
        i += 1
        NameList.append(new_word)


def tipoff(player1, player2):
    goes_to = random.randrange(0, 2)
    if goes_to == 0:
        return player1
    else:
        return player2


def possession(offense, defense):  # Rating has no affect at this point, this function is doodoo rn but its something
    points = random.randrange(2, 4)  # Randomly selects if it is a 2 or a 3
    do_they_score = random.randrange(0, 101)
    if points == 2:
        if do_they_score <= 47:  # 45% chance to score if its a 2 pointer
            offense.score += points
    else:
        if do_they_score <= 36: # 36% chance if its a 3
            offense.score += points


def score(team1, team2):
    print(f'{team1.name}: {team1.score}, {team2.name}: {team2.score}')


def game(team1, team2):
    offense = tipoff(team1, team2)
    quarter = 1
    time_left = 720
    if offense == team1:
        defense = team2
    else:
        defense = team1
    print("Tip goes to the " + offense.name)
    while quarter < 5:
        possession(offense, defense)
        temp = offense
        offense = defense
        defense = temp
        time_left -= random.randrange(10, 25)
        if time_left <= 0:
            quarter += 1
            time_left = 720
    print("Final Score:")
    score(team1, team2)

# If you haven't done anything with python this is basically the start of main in other languages

Mavericks = Team.Team("Mavericks", 90, 78)
Clippers = Team.Team("Clippers", 88, 87)

# These ratings are basically random
Mavericks.players.append(Player.Player("Doncic", "Luka", 95, 82))
Mavericks.players.append(Player.Player("Hardaway jr.", "Tim", 88, 82))
Mavericks.players.append(Player.Player("Finney-Smith", "Dorian", 95, 82))
Mavericks.players.append(Player.Player("Pingus", "Tingus", 82, 75))
Mavericks.players.append(Player.Player("Marjonavic", "Boban", 80, 70))
print(Mavericks.players[0].first)
Mavericks.coach = Coach.Coach("Carlisle", "Rick", 90, 90)


Clippers.players.append(Player.Player("Jackson", "Reggie", 84, 76))
Clippers.players.append(Player.Player("George", "Paul", 95, 88))
Clippers.players.append(Player.Player("Leonard", "Kawhi", 94, 94))
Clippers.players.append(Player.Player("Batum", "Nicholas", 80, 82))
Clippers.players.append(Player.Player("Morris", "Marcus", 82, 80))

Clippers.lineup = Clippers.players
Mavericks.lineup = Mavericks.players

game(Mavericks, Clippers)



