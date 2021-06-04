class Team:
    def __init__(self, teamName, offense, defense):
        self.name = teamName
        self.oRating = offense
        self.dRating = defense
        self.score = 0
        self.players = []
        self.lineup = []