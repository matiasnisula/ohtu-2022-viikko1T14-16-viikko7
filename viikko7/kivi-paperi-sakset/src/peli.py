from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from tekoaly_parannettu import TekoalyParannettu
from tekoaly import Tekoaly

class Peli:

    @staticmethod
    def luo_kaksinpeli():
        return KPSPelaajaVsPelaaja()

    @staticmethod
    def luo_helppo_yksinpeli():
        return KPSTekoaly(Tekoaly())

    @staticmethod
    def luo_vaikea_yksinpeli():
        return KPSParempiTekoaly(TekoalyParannettu(10))
