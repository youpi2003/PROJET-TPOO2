# morpion/classes/Board.py

class Board:
    """
    Classe représentant la grille de jeu du morpion.
    """
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        """
        Affiche la grille.
        """
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def place_symbol(self, row: int, col: int, symbol: str) -> bool:
        """
        Place un symbole sur la grille si la case est vide.
        """
        if 0 <= row < 3 and 0 <= col < 3:
            if self.board[row][col] == " ":
                self.board[row][col] = symbol
                return True
            else:
                print("Case déjà occupée.")
        else:
            print("Coordonnées invalides.")
        return False

    def is_full(self) -> bool:
        """
        Vérifie si la grille est pleine.
        """
        for row in self.board:
            if " " in row:
                return False
        return True

    def check_winner(self) -> str:
        """
        Vérifie s'il y a un gagnant.
        Retourne le symbole gagnant ("X" ou "O") ou une chaîne vide s'il n'y a pas de gagnant.
        """
        # Vérification des lignes
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != " ":
                return row[0]
        # Vérification des colonnes
        for col in range(3):
            if (self.board[0][col] == self.board[1][col] == self.board[2][col] and
                    self.board[0][col] != " "):
                return self.board[0][col]
        # Vérification des diagonales
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != " "):
            return self.board[0][0]
        if (self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != " "):
            return self.board[0][2]
        return ""
