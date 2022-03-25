from kirjanpito import kirjanpito as default_kirjanpito


class Pankki:
    
    def __init__(self, kirjanpito=default_kirjanpito):
        self._kirjanpito = kirjanpito

    def get_kirjanpito(self):
        return self._kirjanpito

    def tilisiirto(self, nimi, viitenumero, tililta, tilille, summa):
        self._kirjanpito.lisaa_tapahtuma(
            f"tilisiirto: tililtä {tililta} tilille {tilille} viite {viitenumero} summa {summa}e"
        )

        # täällä olisi koodi joka ottaa yhteyden pankin verkkorajapintaan
        return True

pankki = Pankki()