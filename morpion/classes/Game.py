# morpion/classes/Game.py

from classes.Board import Board
from classes.Player import Player

class Game:
    """
    Classe représentant une partie de morpion.
    """
    def __init__(self, player1: Player, player2: Player):
        self.board = Board()
        self.players = [player1, player2]
        self.current_player_index = 0

    def switch_player(self):
        """
        Change le joueur courant.
        """
        self.current_player_index = 1 - self.current_player_index

    def play(self):
        """
        Exécute la boucle de jeu.
        """
        while True:
            self.board.display()
            current_player = self.players[self.current_player_index]
            row, col = current_player.get_move()
            if not self.board.place_symbol(row, col, current_player.symbol):
                continue  # la case est occupée ou saisie invalide, refaire le coup

            winner = self.board.check_winner()
            if winner:
                self.board.display()
                print(f"Félicitations {current_player.name}, vous avez gagné!")
                break
            if self.board.is_full():
                self.board.display()
                print("Match nul!")
                break

            self.switch_player()
