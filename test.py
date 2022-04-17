import pickle

players = {"Julien" : {"level" : 0, "score" : 0}, "Maelle" : {"level" : 0, "score" : 0}, "Melody" : {"level" : 0, "score" : 0}}

with open("players.txt", "wb") as file:
    data = pickle.dump(players, file)