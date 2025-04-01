# banque/classes/EmployeBancaire.py

class EmployeBancaire:
    """
    Classe représentant un employé bancaire.
    """
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def consulter_comptes(self, comptes: list):
        """
        Affiche la liste de tous les comptes clients.
        """
        print("Liste des comptes clients :")
        for compte in comptes:
            print(compte)

    def approuver_compte(self, client):
        """
        Simule l'approbation d'un nouveau compte client.
        Par exemple, on pourrait générer un numéro de carte et inviter à définir le PIN.
        """
        print(f"Compte du client {client.nom_complet} approuvé.")
        # Création d'une carte bancaire par exemple :
        from classes.Carte import Carte
        carte = Carte(client.user_id)
        client.ajouter_carte(carte)
        # Vous pourriez ajouter la logique d'invitation à saisir un PIN ici.
        return carte

    def consulter_transactions(self, compte):
        """
        Affiche l'historique des transactions d'un compte.
        """
        print(f"Historique des transactions pour le compte {compte.account_id}:")
        for transaction in compte.transactions:
            print(transaction)

    def geler_compte(self, compte):
        """
        Simule le gel d'un compte.
        """
        print(f"Le compte {compte.account_id} est gelé.")

    def fermer_compte(self, compte):
        """
        Simule la fermeture d'un compte.
        """
        print(f"Le compte {compte.account_id} est fermé.")
