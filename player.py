import json

class Player:
    
    level = 0 #Initiate player's level
    score = 0 #Initiate player's score

    def __init__(self, name):
        self.name = name

    def getPlayerData(self):
        #Return a dictionary with player's data
        with open("players.json", "r") as file:
            data = json.load(file)
        user_dict_init = data[self.name]
        return user_dict_init

    def getPlayerScore(self):
        #Return a string containing player's score
        player_data = self.getPlayerData()
        return player_data["score"]

    def getPlayerLevel(self):
        #Return a string containing player's level
        player_data = self.getPlayerData()
        return player_data["level"]

    def isNameinDatabase(self):
        #Check if player's name is already in the database
        with open("players.json", "r") as file:
            data = json.load(file)
        if self.name in data:
            return True
        else:
            return False

    def setPlayerName(self, name):
        pass
        #Take the name of a new player as an argument
        #Builds a dictionary
        #Check if name is already in the players.json file
        #Write it in the players.json file
        #dict_data_player = {
        #    "name" : self.name,
        #    "level" : self.level,
        #    "score" : self.score
        #    }
        #with open("players.json, "w"):
        #    names = x  

    def setPlayerScore(self, score_added):
        #Sets the player score (With this function the score can only be added)
        pass

###Test###
p1 = Player("Melody")

print(p1.isNameinDatabase())