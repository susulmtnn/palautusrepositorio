from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


class Komentotehdas:
    
    @staticmethod
    def hae(komento):
        komennot = {
            "a": KPSPelaajaVsPelaaja(),
            "b": KPSTekoaly(),
            "c": KPSParempiTekoaly(),
        }
        if komento in komennot:
            return komennot[komento].pelaa()
        else:
            pass