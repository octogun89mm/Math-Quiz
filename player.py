import pickle

class Player:
    
    level = 0 #Initiate player's level
    score = 0 #Initiate player's score

    def __init__(self, name):
        self.name = name

    def getPlayerData(self):
        #Return a dictionary with player's data
        with open("players.txt", "rb") as file:
            data = pickle.load(file)
        if self.name in data:
            return data[self.name]
        else:
            raise "Player isn't in the players.txt file, please create a player first."

    def getPlayerScore(self):
        #Return a integer containing player's score
        player_data = self.getPlayerData()
        return player_data["score"]

    def getPlayerLevel(self):
        #Return a integer containing player's level
        player_data = self.getPlayerData()
        return player_data["level"]

    def isNameinDatabase(self):
        #Check if player's name is already in the database
        with open("players.txt", "rb") as file:
            data = pickle.load(file)
        if self.name in data:
            return True
        else:
            return False

    def setPlayerData(self):
        """- Builds a dictionary
           - Check if name is already in the players.txt file
           - Write it in the players.txt file"""
        isNameinDatabase = self.isNameinDatabase()
        if isNameinDatabase == True:
            return "Name is already in database, can't initiate new player data in players.txt file."
        elif isNameinDatabase == False:
            dict_data_player = {"level" : self.level, "score" : self.score} #Initiate a dictionnary with new player data
            with open("players.txt", "rb") as file: #Open players.txt to later append new players data
                data = pickle.load(file)
            data[self.name] = dict_data_player
            with open("players.txt", "wb") as file:
                pickle.dump(data, file)

    def setPlayerScore(self, score_added):
        #Sets the player score (With this function the score can only be added)
        pass

    def deletePlayer(self):
        with open("players.txt", "rb") as file:
            data = pickle.load(file)
        del data[self.name]
        with open("players.txt", "wb") as file:
            pickle.dump(data, file)

###Test###
p1 = Player("Robert")

print(p1.deletePlayer())