from tuomari import Tuomari
from kivipaperisakset import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
        # tuomari = Tuomari()

        # ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        # tokan_siirto = input("Toisen pelaajan siirto: ")

        # while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
        #     tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
        #     print(tuomari)

        #     ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        #     tokan_siirto = input("Toisen pelaajan siirto: ")

        # print("Kiitos!")
        # print(tuomari)

    def _toisen_siirto(self, ensimmäisen_siirto):
        tokan_siirto=input("Toisen pelaajan siirto: ")

        return tokan_siirto
