class Player:
    def __init__(self, last, first):
        self.team = "Free Agent"
        self.first = first
        self.last = last
        self.updatedStats = False
        self.stats = []
        self.seasonsLoaded = 0

    def __init__(self, last, first, team):
        self.team = team
        self.first = first
        self.last = last
        self.updatedStats = False
        self.stats = []
        self.college = 'N/A'
        self.seasonsLoaded = 0








