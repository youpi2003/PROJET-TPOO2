# banque/classes/ClientEntreprise.py

from classes.Compte import Compte

class ClientEntreprise:
    """
    Classe représentant un client entreprise.
    Le compte est partagé par les employés autorisés.
    """
    def __init__(self, company_id: str, nom_entreprise: str, adresse: str,
                 num_fiscal: str, account_id: str, password: str,
                 estimated_withdrawal_limit: float):
        self.company_id = company_id
        self.nom_entreprise = nom_entreprise
        self.adresse = adresse
        self.num_fiscal = num_fiscal
        self.account_id = account_id
        self.password = password
        self.compte = Compte(account_id=account_id, withdrawal_limit=estimated_withdrawal_limit)
        self.employes_ids = []  # Liste des user_ids des employés

    def ajouter_employe(self, user_id: str):
        """
        Ajoute un employé à l'entreprise.
        """
        if user_id not in self.employes_ids:
            self.employes_ids.append(user_id)

    def deposer(self, amount: float) -> bool:
        return self.compte.deposit(amount)

    def retirer(self, amount: float) -> bool:
        return self.compte.withdraw(amount)

    def transferer_vers_utilisateur(self, amount: float, destination: 'ClientEntreprise' or object) -> bool:
        """
        Transférer des fonds vers un client utilisateur.
        On peut vérifier ici que destination est bien un client utilisateur.
        """
        # On s'attend à ce que destination ait un attribut 'compte'
        return self.compte.transfer(amount, destination.compte)

    def consulter_solde(self) -> float:
        return self.compte.balance

    def historique_transactions(self):
        for transaction in self.compte.transactions:
            print(transaction)

    def demander_pret(self, montant: float):
        """
        Méthode simulant une demande de prêt.
        """
        print(f"La demande de prêt de {montant} FCFA pour {self.nom_entreprise} est en attente d'approbation.")

    def __str__(self):
        return f"Entreprise {self.nom_entreprise} ({self.company_id}) - Compte: {self.compte}"
