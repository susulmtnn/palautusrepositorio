from tekoaly_parannettu import TekoalyParannettu
from kivipaperisakset import KiviPaperiSakset

class KPSParempiTekoaly(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmäisen_siirto):

        tekoaly = TekoalyParannettu(10)
        tokan_siirto=tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")

        return tokan_siirto