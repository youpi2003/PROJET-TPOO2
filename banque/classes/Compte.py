# banque/classes/Compte.py

class Compte:
    """
    Classe représentant un compte bancaire.
    Le type de compte (Bronze, Or, Affaires) est déterminé selon la limite quotidienne de retrait.
    """

    def __init__(self, account_id: str, withdrawal_limit: float):
        self.account_id = account_id
        self.balance = 0.0  # solde initial
        self.withdrawal_limit = withdrawal_limit
        self.account_type = self._determine_type(withdrawal_limit)
        self.transactions = []  # historique des transactions

    def _determine_type(self, limit: float) -> str:
        """
        Détermine le type de compte en fonction de la limite de retrait journalière.
        """
        if limit <= 500000:
            return "Bronze"
        elif limit <= 1000000:
            return "Or"
        else:
            return "Affaires"

    def deposit(self, amount: float) -> bool:
        """
        Déposer une somme sur le compte.
        """
        if amount <= 0:
            print("Le montant à déposer doit être positif.")
            return False
        self.balance += amount
        self.transactions.append(("Dépôt", amount))
        return True

    def withdraw(self, amount: float) -> bool:
        """
        Retirer une somme du compte en respectant le solde et la limite de retrait.
        """
        if amount <= 0:
            print("Le montant à retirer doit être positif.")
            return False
        if amount > self.balance:
            print("Fonds insuffisants.")
            return False
        if amount > self.withdrawal_limit:
            print("Montant supérieur à la limite quotidienne de retrait.")
            return False
        self.balance -= amount
        self.transactions.append(("Retrait", amount))
        return True

    def transfer(self, amount: float, destination: 'Compte') -> bool:
        """
        Transférer une somme vers un autre compte.
        """
        if self.withdraw(amount):
            destination.deposit(amount)
            self.transactions.append(("Transfert vers", destination.account_id, amount))
            return True
        return False

    def __str__(self):
        return (f"Compte {self.account_id} - Type: {self.account_type} - "
                f"Solde: {self.balance} - Limite: {self.withdrawal_limit}")
