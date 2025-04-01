# banque/classes/ClientUtilisateur.py

from classes.Compte import Compte
from classes.Carte import Carte

class ClientUtilisateur:
    """
    Classe représentant un client utilisateur.
    Possède un compte bancaire et peut détenir une ou plusieurs cartes.
    """
    def __init__(self, user_id: str, nom_complet: str, adresse: str,
                 telephone: str, cnic: str, login: str, password: str,
                 estimated_withdrawal_limit: float):
        self.user_id = user_id
        self.nom_complet = nom_complet
        self.adresse = adresse
        self.telephone = telephone
        self.cnic = cnic
        self.login = login
        self.password = password
        self.compte = Compte(account_id=user_id, withdrawal_limit=estimated_withdrawal_limit)
        self.cartes = []  # Liste d'objets Carte

    def ajouter_carte(self, carte: Carte):
        """
        Ajoute une nouvelle carte au client.
        """
        self.cartes.append(carte)

    def deposer(self, amount: float) -> bool:
        return self.compte.deposit(amount)

    def retirer(self, amount: float, carte: Carte, pin: str) -> bool:
        """
        Retirer de l'argent en vérifiant le PIN de la carte.
        """
        if carte.verify_pin(pin):
            return self.compte.withdraw(amount)
        else:
            print("Transaction refusée à cause d'une erreur PIN.")
            return False

    def transferer(self, amount: float, destination: 'ClientUtilisateur', carte: Carte, pin: str) -> bool:
        """
        Transférer des fonds vers un autre client après vérification du PIN.
        """
        if carte.verify_pin(pin):
            return self.compte.transfer(amount, destination.compte)
        else:
            print("Transaction de transfert refusée en raison d'un PIN incorrect.")
            return False

    def consulter_solde(self) -> float:
        return self.compte.balance

    def historique_transactions(self):
        for transaction in self.compte.transactions:
            print(transaction)

    def __str__(self):
        return f"Client {self.nom_complet} ({self.user_id}) - Compte: {self.compte}"
