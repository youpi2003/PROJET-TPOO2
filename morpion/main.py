# morpion/main.py

from classes.Player import Player
from classes.Game import Game

def main():
    print("Bienvenue dans le jeu du Morpion !")
    name1 = input("Entrez le nom du premier joueur: ")
    name2 = input("Entrez le nom du deuxième joueur: ")

    player1 = Player(name1, "X")
    player2 = Player(name2, "O")

    game = Game(player1, player2)
    game.play()

if __name__ == "__main__":
    main()
