class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team=dict['team']
        self.goals=dict['goals']
        self.assists=dict['assists']
        self.nationality=dict['nationality']
        self.total=self.assists+self.goals
    
    def __str__(self):
        return self.name + " team " + self.team + " goals " + str(self.goals) + " assists " + str(self.assists) + " " + self.nationality