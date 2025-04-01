# morpion/classes/Player.py

class Player:
    """
    Classe représentant un joueur de morpion.
    """
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol

    def get_move(self):
        """
        Obtient le coup du joueur via une saisie console.
        Retourne une paire (row, col).
        """
        try:
            move = input(f"{self.name} ({self.symbol}), entrez votre coup (ligne,colonne) : ")
            row, col = move.strip().split(',')
            return int(row), int(col)
        except Exception as e:
            print("Saisie invalide. Veuillez entrer au format 'ligne,colonne' (ex: 1,2).")
            return self.get_move()

    def __str__(self):
        return f"{self.name} ({self.symbol})"
