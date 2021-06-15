import Stat
import Team
import Player
import Coach
import Season
import Month
import Day
import time

import math
import random
import pandas as pd
from guppy import hpy
h = hpy()


def make_team(team_name, path):  #
    new_team = Team.Team(team_name)
    df = pd.read_csv(path)

    for index, row in df.iterrows():
        name = row['Player'].split()
        the_player = Player.Player(name[1], name[0], team_name)
        the_player.pos = row['Pos']
        the_player.height = row['Ht']
        the_player.weight = row['Wt']
        birthday = row['Birth Date'].split()
        the_player.bYear = birthday[2]
        the_player.bDay = birthday[1]
        the_player.bMonth = birthday[0]
        the_player.exp = row['Exp']
        the_player.college = row['College']
        new_team.players.append(the_player)
        players.append(the_player)
    return new_team


def make_standard_nba_rosters(path):
    the_teams = [make_team("Atlanta Hawks", path + "/Atlanta.csv"), make_team("Boston Celtics", path + "/Boston.csv"),
                 make_team("Brooklyn Nets", path + "/Brooklyn.csv"),
                 make_team("Charlotte Hornets", path + "/Charlotte.csv"),
                 make_team("Chicago Bulls", path + "/Chicago.csv"),
                 make_team("Cleveland Cavaliers", path + "/Cleveland.csv"),
                 make_team("Dallas Mavericks", path + "/Dallas.csv"), make_team("Denver Nuggets", path + "/Denver.csv"),
                 make_team("Detroit Pistons", path + "/Detroit.csv"),
                 make_team("Golden State Warriors", path + "/Golden State.csv"),
                 make_team("Houston Rockets", path + "/Houston.csv"),
                 make_team("Indiana Pacers", path + "/Indiana.csv"),
                 make_team("New York Knicks", path + "/Knickerbockers.csv"),
                 make_team("Los Angeles Clippers", path + "/LAC.csv"),
                 make_team("Los Angeles Lakers", path + "/LAL.csv"),
                 make_team("Memphis Grizzlies", path + "/Memphis.csv"), make_team("Miami Heat", path + "/Miami.csv"),
                 make_team("Milwaukee Bucks", path + "/Milwaukee.csv"),
                 make_team("Minnesota Timberwolves", path + "/Minnesota.csv"),
                 make_team("New Orleans Pelicans", path + "/New Orleans.csv"),
                 make_team("Oklahoma City Thunder", path + "/OKC.csv"),
                 make_team("Orlando Magic", path + "/Orlando.csv"),
                 make_team("Philadelphia 76ers", path + "/Philly.csv"),
                 make_team("Phoenix Suns", path + "/Phoenix.csv"),
                 make_team("Portland Trail Blazers", path + "/Portland.csv"),
                 make_team("Sacramento Kings", path + "/Sacramento.csv"),
                 make_team("San Antonio Spurs", path + "/San Antonio.csv"),
                 make_team("Toronto Raptors", path + "/Toronto.csv"), make_team("Utah Jazz", path + "/Utah.csv"),
                 make_team("Washington Wizards", path + "/Washington.csv")]
    return the_teams


def assign_player_stats():  # Attaches stats to each player
    advanced = pd.read_csv("Stats/20-21 Advanced.csv")
    totals = pd.read_csv("Stats/20-21 Totals.csv")
    shooting = pd.read_csv("Stats/20-21 Shooting.csv")

    # at first these stat names were variable names, eventually realized it was easier to make a stat class. I'll go
    # back thru later and make better names
    for index, row in advanced.iterrows():
        name = row['Player'].split("\\")
        name = name[0].split()
        the_player = next((x for x in players if x.first == name[0] and x.last == name[1]), "Not found")
        if the_player != "Not found":
            the_player.updatedStats = True
            the_player.stats.append(Stat.Stat("PER", row['PER']))
            the_player.stats.append(Stat.Stat("FTr", row['FTr']))
            the_player.stats.append(Stat.Stat("TRBPerc", row['TRB%']))
            the_player.stats.append(Stat.Stat("Usage", row['USG%']))

    for index, row in totals.iterrows():
        name = row['Player'].split("\\")
        name = name[0].split()
        the_player = next((x for x in players if x.first == name[0] and x.last == name[1]), "Not found")
        if the_player != "Not found":
            games_played = row['G']
            the_player.stats.append(Stat.Stat("games played", games_played))
            the_player.stats.append(Stat.Stat("2P%", row['2P%']))
            the_player.stats.append(Stat.Stat("twoAtt", row['2PA']))
            the_player.stats.append(Stat.Stat("threePerc", row['3P%']))
            the_player.stats.append(Stat.Stat("MP", row['MP']))
            the_player.stats.append(Stat.Stat("FTA", row['FTA']))
            the_player.stats.append(Stat.Stat("FTPerc", row['FT%']))
            the_player.stats.append(Stat.Stat("TRB", row['TRB']))
            if row['TOV'] != 0:
                the_player.stats.append(Stat.Stat("AtoT", row['AST'] / row['TOV']))
            else:
                the_player.stats.append(Stat.Stat("AtoT", 1.7))
            if games_played != 0:
                the_player.stats.append(Stat.Stat("ORBG", row['ORB'] / games_played))
                the_player.stats.append(Stat.Stat("DRBG", row['DRB'] / games_played))
                the_player.stats.append(Stat.Stat("APG", row['AST'] / games_played))
                the_player.stats.append(Stat.Stat("PPG", row['PTS'] / games_played))
                the_player.stats.append(Stat.Stat("threeAtt", round(row['3PA'] / games_played, 3)))
            else:
                the_player.stats.append(Stat.Stat("ORBG", math.nan))
                the_player.stats.append(Stat.Stat("DRBG", math.nan))
                the_player.stats.append(Stat.Stat("APG", math.nan))
                the_player.stats.append(Stat.Stat("PPG", math.nan))
                the_player.stats.append(Stat.Stat("threeAtt", math.nan))

    for index, row in shooting.iterrows():
        name = row['Player'].split("\\")
        name = name[0].split()
        the_player = next((x for x in players if x.first == name[0] and x.last == name[1]), "Not found")
        if the_player != "Not found":
            the_player.seasonsLoaded += 1
            the_player.stats.append(Stat.Stat("avgDist", row['Dist.']))
            the_player.stats.append(Stat.Stat("percAttTwoPoint", row['2P d']))
            the_player.stats.append(Stat.Stat("percAttInside", row['0-3 d']))
            the_player.stats.append(Stat.Stat("percAttShortMid", row['3-10 d']))
            the_player.stats.append(Stat.Stat("percAttMid", row['10-16 d']))
            the_player.stats.append(Stat.Stat("percAttDeepMid", row['16-3P d']))
            the_player.stats.append(Stat.Stat("percAttThree", row['3P d']))

            the_player.stats.append(Stat.Stat("FGpercTwoPoint", row['2P p']))
            the_player.stats.append(Stat.Stat("FGpercAttInside", row['0-3 p']))
            the_player.stats.append(Stat.Stat("FGpercAttShortMid", row['3-10 p']))
            the_player.stats.append(Stat.Stat("FGpercAttMid", row['10-16 p']))
            the_player.stats.append(Stat.Stat("FGpercDeepMid", row['16-3P p']))
            the_player.stats.append(Stat.Stat("FGpercThree", row['3P p']))

            the_player.stats.append(Stat.Stat("assistedTwos", row['2P a']))
            the_player.stats.append(Stat.Stat("assistedThrees", row['3P a']))

            the_player.stats.append(Stat.Stat("percDunks", row['%FGA du']))
            the_player.stats.append(Stat.Stat("cornerThreeAtt", row['%3PA c']))
            the_player.stats.append(Stat.Stat("cornerThree", row['3P% c']))

    advanced = pd.read_csv('Stats/19-20 Advanced.csv')
    totals = pd.read_csv('Stats/19-20 Totals.csv')
    shooting = pd.read_csv('Stats/19-20 Shooting.csv')

    # right now it only adds 19-20 stats if they werent present in the 20-21 stats file, but eventually I want a list
    # of past seasons stats where more recent seasons are more heavily weighted. Young players will have a much
    # stronger weight on their most recent season
    for index, row in advanced.iterrows():
        name = row['Player'].split("\\")
        name = name[0].split()
        the_player = next((x for x in players if x.first == name[0] and x.last == name[1]), "Not found")
        if the_player != "Not found" and the_player.seasonsLoaded == 0:
            the_player.updatedStats = True
            the_player.stats.append(Stat.Stat("PER", row['PER']))
            the_player.stats.append(Stat.Stat("FTr", row['FTr']))
            the_player.stats.append(Stat.Stat("TRBPerc", row['TRB%']))
            the_player.stats.append(Stat.Stat("Usage", row['USG%']))

    for index, row in totals.iterrows():
        name = row['Player'].split("\\")
        name = name[0].split()
        the_player = next((x for x in players if x.first == name[0] and x.last == name[1]), "Not found")
        if the_player != "Not found" and the_player.seasonsLoaded == 0:
            games_played = row['G']
            the_player.stats.append(Stat.Stat("games played", games_played))
            the_player.stats.append(Stat.Stat("2P%", row['2P%']))
            the_player.stats.append(Stat.Stat("twoAtt", row['2PA']))
            the_player.stats.append(Stat.Stat("threePerc", row['3P%']))
            the_player.stats.append(Stat.Stat("MP", row['MP']))
            the_player.stats.append(Stat.Stat("FTA", row['FTA']))
            the_player.stats.append(Stat.Stat("FTPerc", row['FT%']))
            the_player.stats.append(Stat.Stat("TRB", row['TRB']))
            if row['TOV'] != 0:
                the_player.stats.append(Stat.Stat("AtoT", row['AST'] / row['TOV']))
            else:
                the_player.stats.append(Stat.Stat("AtoT", 1.7))
            if games_played != 0:
                the_player.stats.append(Stat.Stat("ORBG", row['ORB'] / games_played))
                the_player.stats.append(Stat.Stat("DRBG", row['DRB'] / games_played))
                the_player.stats.append(Stat.Stat("APG", row['AST'] / games_played))
                the_player.stats.append(Stat.Stat("PPG", row['PTS'] / games_played))
                the_player.stats.append(Stat.Stat("threeAtt", round(row['3PA'] / games_played, 3)))
            else:
                the_player.stats.append(Stat.Stat("ORBG", math.nan))
                the_player.stats.append(Stat.Stat("DRBG", math.nan))
                the_player.stats.append(Stat.Stat("APG", math.nan))
                the_player.stats.append(Stat.Stat("PPG", math.nan))
                the_player.stats.append(Stat.Stat("threeAtt", math.nan))

    for index, row in shooting.iterrows():
        name = row['Player'].split("\\")
        name = name[0].split()
        the_player = next((x for x in players if x.first == name[0] and x.last == name[1]), "Not found")
        if the_player != "Not found" and the_player.seasonsLoaded == 0:
            the_player.seasonsLoaded += 1
            the_player.stats.append(Stat.Stat("avgDist", row['Dist.']))
            the_player.stats.append(Stat.Stat("percAttTwoPoint", row['2P d']))
            the_player.stats.append(Stat.Stat("percAttInside", row['0-3 d']))
            the_player.stats.append(Stat.Stat("percAttShortMid", row['3-10 d']))
            the_player.stats.append(Stat.Stat("percAttMid", row['10-16 d']))
            the_player.stats.append(Stat.Stat("percAttDeepMid", row['16-3P d']))
            the_player.stats.append(Stat.Stat("percAttThree", row['3P d']))

            the_player.stats.append(Stat.Stat("FGpercTwoPoint", row['2P p']))
            the_player.stats.append(Stat.Stat("FGpercAttInside", row['0-3 p']))
            the_player.stats.append(Stat.Stat("FGpercAttShortMid", row['3-10 p']))
            the_player.stats.append(Stat.Stat("FGpercAttMid", row['10-16 p']))
            the_player.stats.append(Stat.Stat("FGpercDeepMid", row['16-3P p']))
            the_player.stats.append(Stat.Stat("FGpercThree", row['3P p']))

            the_player.stats.append(Stat.Stat("assistedTwos", row['2P a']))
            the_player.stats.append(Stat.Stat("assistedThrees", row['3P a']))

            the_player.stats.append(Stat.Stat("percDunks", row['%FGA du']))
            the_player.stats.append(Stat.Stat("cornerThreeAtt", row['%3PA c']))
            the_player.stats.append(Stat.Stat("cornerThree", row['3P% c']))


def clean_player_stats():  # incomplete, not sure how to handle every stat
    for player in players:
        thing = False
        for stat in player.stats:
            if pd.isna(stat.number):
                if "THREE" in stat.name.upper():
                    stat.number = 0
                    if thing is False:
                        thing = True
                        print(f'{player.first} {player.last}')
                else:
                    pass
                    # print(stat.name)


def assign_team_stats():
    df = pd.read_csv("Stats/20-21 Teams_Advanced.csv")
    for index, row in df.iterrows():
        name = row['Team']
        team = next(x for x in teams if x.name == name)
        team.pace = row['Pace']
        team.threePAr = row['3PAr']
        team.FTr = row['FTr']
        team.OTOVrate = row['TOV% o']
        team.DROVrate = row['TOV% d']
        team.Dfouls = row['FT/FGA d']


def populate_season(year):  # will come into play implementing the GM/Coach Mode
    season = Season.Season(year)
    season.months.append(Month.Month("January", 31))
    season.months.append(Month.Month("February", 28))
    season.months.append(Month.Month("March", 31))
    season.months.append(Month.Month("April", 30))
    season.months.append(Month.Month("May", 31))
    season.months.append(Month.Month("June", 30))
    season.months.append(Month.Month("July", 31))
    season.months.append(Month.Month("August", 31))
    season.months.append(Month.Month("September", 30))
    season.months.append(Month.Month("October", 31))
    season.months.append(Month.Month("November", 30))
    season.months.append(Month.Month("December", 31))
    return season


def name_list_maker(names):  # WIll come in handy dealing with generated rookie names in the future
    i = 0
    name_list = []
    while i < len(names):
        new_word = ""
        while names[i] != " ":
            new_word = new_word + names[i]
            i += 1
            if i >= len(names):
                name_list.append(new_word)
                return name_list
        i += 1
        name_list.append(new_word)


def tipoff(player1, player2): # add probability based on height, and jumping when thats added
    goes_to = random.randrange(0, 2)
    if goes_to == 0:
        return player1
    else:
        return player2


def possession(ball_handler):  # does nothing atm, but can be worked on now that stats are in
    pass


def score(team1, team2):
    print(f'{team1.name}: {team1.score}, {team2.name}: {team2.score}')


def game(team1, team2):  # Basic game structure, needs work. Team's Pace should be included
    offense = tipoff(team1, team2)
    quarter = 1
    time_left = 720
    if offense == team1:
        defense = team2
    else:
        defense = team1
    print("Tip goes to the " + offense.name)
    while quarter < 5:
        possession(offense.ballhandlers[0])
        temp = offense
        offense = defense
        defense = temp
        time_left -= random.randrange(10, 25)
        if time_left <= 0:
            quarter += 1
            time_left = 720
    print("Final Score:")
    score(team1, team2)


start = time.time()
players = []
# check_if_changes()
teams = make_standard_nba_rosters("Rosters")
assign_player_stats()
clean_player_stats()
assign_team_stats()

stop = time.time()
# print(stop - start)

# for player in players:
#   print(f'{player.first} {player.last}:')
#  print(f'{player.bMonth} {player.bDay}, {player.bYear}')
# print(f'Went to {player.college}')
