class Player:

    level = 0 #Initiate player's level
    score = 0 #Initiate player's score

    def __init__(self, name):
        self.name = name

    def getPlayerData(self):
        #Take name of the player as an argument and return a dictionary with player's data
        import json
        with open("players.json", "r") as file:
            data = json.load(file)
        user_dict_init = data[self.name]
        return user_dict_init[0]
    
    def isNameinDatabase(self, name):
        #Check if player's name is already in the database
        pass
    
    def setPlayerScore(self, score_added):
        #Sets the player score (With this function the score can only be added)
        pass

###Test###
p1 = Player("Julien")

player_data = p1.getPlayerData()

print(player_data["score"])