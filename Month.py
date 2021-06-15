import Day


class Month:
    def __init__(self, name, days):
        self.name = name
        self.days = []
        i = 0
        while i < days:
            self.days.append(Day.Day(i))
