from classes.ClientUtilisateur import ClientUtilisateur
from classes.ClientEntreprise import ClientEntreprise
from classes.EmployeBancaire import EmployeBancaire
from classes.Transaction import Transaction
from classes.Carte import Carte

def saisir_montant(message):
    while True:
        try:
            montant = float(input(message))
            if montant < 0:
                print("Le montant ne peut pas être négatif.")
                continue
            return montant
        except ValueError:
            print("Veuillez entrer un montant valide.")

def main():
    print("--- Création d'un client utilisateur ---")
    user_id = input("ID utilisateur : ")
    nom_complet = input("Nom complet : ")
    adresse = input("Adresse : ")
    telephone = input("Téléphone : ")
    cin = input("CIN : ")
    login = input("Login : ")
    password = input("Mot de passe : ")
    estimated_limit = saisir_montant("Limite de retrait estimée : ")
    
    client1 = ClientUtilisateur(user_id, nom_complet, adresse, telephone, cin, login, password, estimated_limit)
    
    print("\n--- Dépôt initial ---")
    montant_depot = saisir_montant("Montant à déposer : ")
    client1.deposer(montant_depot)
    
    print("\n--- Création d'une carte bancaire ---")
    carte = Carte(client1.user_id)
    pin = input("Définissez un code PIN : ")
    carte.set_pin(pin)
    client1.ajouter_carte(carte)
    
    print("\n--- Création d'une entreprise ---")
    company_id = input("ID entreprise : ")
    nom_entreprise = input("Nom de l'entreprise : ")
    adresse_entreprise = input("Adresse entreprise : ")
    num_fiscal = input("Numéro fiscal : ")
    account_id = input("ID du compte entreprise : ")
    password_entreprise = input("Mot de passe entreprise : ")
    estimated_limit_entreprise = saisir_montant("Limite de retrait estimée : ")
    
    entreprise = ClientEntreprise(company_id, nom_entreprise, adresse_entreprise, num_fiscal, account_id, password_entreprise, estimated_limit_entreprise)
    
    print("\n--- Dépôt initial entreprise ---")
    montant_depot_entreprise = saisir_montant("Montant à déposer : ")
    entreprise.deposer(montant_depot_entreprise)
    
    print("\n--- Effectuer un transfert ---")
    montant_transfert = saisir_montant("Montant à transférer : ")
    pin_transfert = input("Entrez votre PIN pour valider : ")
    
    if client1.transferer(montant_transfert, entreprise, carte, pin_transfert):
        print("Transfert effectué avec succès.")
    else:
        print("Transfert échoué.")
    
    print("\n--- Consultation des comptes ---")
    print(client1)
    client1.historique_transactions()
    
    print(entreprise)
    entreprise.historique_transactions()
    
    employe = EmployeBancaire(username="admin", password="adminpass")
    comptes = [client1.compte, entreprise.compte]
    print("\n--- Consultation par l'employé bancaire ---")
    employe.consulter_comptes(comptes)

if __name__ == "__main__":
    main()
