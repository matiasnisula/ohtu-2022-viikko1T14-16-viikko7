from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostokset_lista = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        tavaroita = 0
        for ostos in self.ostokset_lista:
            tavaroita += ostos.lukumaara()
        return tavaroita
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0
        for ostos in self.ostokset_lista:
            hinta += ostos.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self.ostokset_lista:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                return
        self.ostokset_lista.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for i in range(len(self.ostokset_lista)):

            if self.ostokset_lista[i].tuotteen_nimi() == poistettava.nimi():
                self.ostokset_lista[i].muuta_lukumaaraa(-1)

                if self.ostokset_lista[i].lukumaara() == 0:
                    self.ostokset_lista.pop(i)


    def tyhjenna(self):
        self.ostokset_lista.clear()
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostokset_lista
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
