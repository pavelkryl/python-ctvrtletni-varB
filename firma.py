from dataclasses import dataclass


@dataclass 
class Karta:
    id: str

class Zamestnanec:
    
    def __init__(self, jmeno, prijmeni):
        self._jmeno = jmeno
        self._prijmeni = prijmeni
        self._karty = []

    def pridej(karta):
        """
        Funkce prida kartu do 'karty', pokud jeste v seznamu neni
        """

    def kontrola(id_karty):
        """
        funkce vraci true, pokud id_karty odpovida nejake karte zamestnance, jinak false
        """
        ...
        


"""
pouze oktavy:
- napiste spravne typove anotace, tak aby mypy nehlasilo zadne chyby ve striktnim modu
- napiste tridu Vratny:
    - bude mit kontejner zamestnancu (se spravne nastavenymi kartami)
    - bude mit metodu pustit():
        - vstup: id karty
        - vystup: true nebo false, podle toho, zda nektery ze zamestnancu kartu ma nebo ne
        - zkuste naprogramovat optimalne, kdyz ne nevadi, alespon funkcne

"""
