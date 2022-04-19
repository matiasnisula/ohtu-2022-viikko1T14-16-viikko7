class Summa:
    def __init__(self, sovelluslogiikka, syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote
        self._alkutila = 0
    
    def suorita(self):
        self._alkutila = self._sovelluslogiikka.tulos
        self._sovelluslogiikka.plus(int(self._syote()))
    
    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._alkutila)

class Erotus:
    def __init__(self, sovelluslogiikka, syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote
        self._alkutila = 0

    def suorita(self):
        self._alkutila = self._sovelluslogiikka.tulos
        self._sovelluslogiikka.miinus(int(self._syote()))

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._alkutila)

class Nollaus:
    def __init__(self, sovelluslogiikka, syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote
        self._alkutila = 0

    def suorita(self):
        self._alkutila = self._sovelluslogiikka.tulos
        self._sovelluslogiikka.nollaa()

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._alkutila)

class Kumoa:
    def __init__(self):
        self._edellinen_komento = None
    
    def aseta_komento(self, komento):
        self._edellinen_komento = komento

    def suorita(self):
        self._edellinen_komento.kumoa()