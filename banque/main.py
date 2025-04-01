# banque/main.py

from classes.ClientUtilisateur import ClientUtilisateur
from classes.ClientEntreprise import ClientEntreprise
from classes.EmployeBancaire import EmployeBancaire
from classes.Transaction import Transaction

def main():
    # Création d'un client utilisateur
    client1 = ClientUtilisateur(
        user_id="U001",
        nom_complet="Alice Dupont",
        adresse="10 Rue de la République",
        telephone="0123456789",
        cnic="CNI123456",
        login="alice",
        password="passAlice",
        estimated_withdrawal_limit=500000
    )

    # Simuler un dépôt
    client1.deposer(300000)
    # Simuler un retrait (avec une carte : pour la démonstration, on crée une carte et on fixe le PIN)
    if client1.cartes:
        carte = client1.cartes[0]
    else:
        # Pour simplifier, on crée et ajoute une carte
        from classes.Carte import Carte
        carte = Carte(client1.user_id)
        carte.set_pin("1234")
        client1.ajouter_carte(carte)

    client1.retirer(100000, carte, "1234")

    # Création d'un client entreprise
    entreprise = ClientEntreprise(
        company_id="E001",
        nom_entreprise="TechCorp",
        adresse="20 Avenue de l'Innovation",
        num_fiscal="TAX987654",
        account_id="E001_COMP",
        password="passTech",
        estimated_withdrawal_limit=20000000
    )
    entreprise.deposer(5000000)
    entreprise.retirer(2000000)

    # Simulation d'une opération de transfert entre client et entreprise
    print("\nTransfert de fonds de client vers entreprise (simulation) :")
    client1.deposer(200000)  # nouveau dépôt pour avoir le montant
    if client1.transferer(150000, entreprise, carte, "1234"):
        print("Transfert effectué avec succès.")
    else:
        print("Transfert échoué.")

    # Consultation des soldes et transactions
    print("\n--- Détails du compte utilisateur ---")
    print(client1)
    client1.historique_transactions()

    print("\n--- Détails du compte entreprise ---")
    print(entreprise)
    entreprise.historique_transactions()

    # Employé bancaire qui consulte les comptes
    employe = EmployeBancaire(username="admin", password="adminpass")
    comptes = [client1.compte, entreprise.compte]
    print("\n--- Consultation par l'employé bancaire ---")
    employe.consulter_comptes(comptes)

if __name__ == "__main__":
    main()
