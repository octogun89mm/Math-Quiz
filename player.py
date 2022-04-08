class Player:

    level = 0
    score = 0
    name = "John"

    def __init__(self, name, score, level):
        self.name = name
        self.score = score
        self.level = level

    def getPlayerName(self):
        ASK_PLAYER_NAME = "What's your name?: "
        name = input(ASK_PLAYER_NAME)
        return name
    
    def isNameinDatabase(self, name):
        pass
    
    def setPlayerScore(self, score_added):
        pass
