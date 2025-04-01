# banque/classes/Carte.py
import random

class Carte:
    """
    Classe représentant une carte bancaire.
    Attribuée à un client une fois son compte approuvé.
    """
    def __init__(self, client_user_id: str, pin: str = None):
        self.client_user_id = client_user_id
        self.card_number = self._generate_card_number()
        # Si aucun PIN n'est fourni, on invite à le définir ultérieurement
        self.pin = pin if pin is not None else ""
        self.failed_attempts = 0
        self.blocked = False

    def _generate_card_number(self) -> str:
        """
        Génère un numéro de carte à 16 chiffres aléatoirement.
        """
        return ''.join([str(random.randint(0, 9)) for _ in range(16)])

    def set_pin(self, new_pin: str):
        """
        Définit ou modifie le PIN de la carte.
        """
        self.pin = new_pin
        self.failed_attempts = 0
        self.blocked = False

    def verify_pin(self, input_pin: str) -> bool:
        """
        Vérifie le PIN entré. Si trois tentatives échouent, la carte est bloquée.
        """
        if self.blocked:
            print("Carte bloquée en raison de tentatives infructueuses.")
            return False
        if input_pin == self.pin:
            self.failed_attempts = 0
            return True
        else:
            self.failed_attempts += 1
            print("PIN incorrect.")
            if self.failed_attempts >= 3:
                self.blocked = True
                print("Carte bloquée après 3 tentatives infructueuses.")
            return False

    def __str__(self):
        status = "Bloquée" if self.blocked else "Active"
        return f"Carte {self.card_number} (Client {self.client_user_id}) - {status}"
