from tuomari import Tuomari
from kivipaperisakset import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmäisen_siirto):
        tokan_siirto=input("Toisen pelaajan siirto: ")

        return tokan_siirto
