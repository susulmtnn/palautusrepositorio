from tuomari import Tuomari
from tekoaly import Tekoaly
from kivipaperisakset import KiviPaperiSakset


class KPSTekoaly(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmäisen_siirto):
        tekoaly = Tekoaly()
        tokan_siirto=tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")

        return tokan_siirto
