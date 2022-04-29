from tekoaly import Tekoaly
from kps import KPS


class KPSTekoaly(KPS):
    def __init__(self, tekoaly):
        self.tekoaly = tekoaly

    def _toisen_siirto(self, ensimmaisen_siirto):     
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        toisen_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {toisen_siirto}")
        return toisen_siirto
