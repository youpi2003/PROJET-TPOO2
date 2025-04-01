# banque/classes/Transaction.py
from datetime import datetime

class Transaction:
    """
    Classe représentant une transaction bancaire.
    """
    def __init__(self, client_user_id: str, amount: float, transaction_type: str, 
                 destination_id: str = None):
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.client_user_id = client_user_id
        self.amount = amount
        self.transaction_type = transaction_type  # "Dépôt", "Retrait", "Transfert"
        self.destination_id = destination_id

    def __str__(self):
        base = f"{self.date} | Client {self.client_user_id} | {self.amount} FCFA | {self.transaction_type}"
        if self.destination_id:
            base += f" -> {self.destination_id}"
        return base
