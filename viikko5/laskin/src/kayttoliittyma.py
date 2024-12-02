from enum import Enum
from tkinter import ttk, constants, StringVar


EDELLINEN_LUKU=0

class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root

        self._komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka, self._lue_syote),
            Komento.EROTUS: Erotus(sovelluslogiikka, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovelluslogiikka, self._lue_syote),
            Komento.KUMOA: Kumoa(sovelluslogiikka, self._lue_syote) # ei ehkä tarvita täällä...
        }

    def _lue_syote(self):
        return self._syote_kentta.get()
    
    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)


    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        komento_olio.suorita()

        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
            self._kumoa_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL
            self._kumoa_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())

class Laskutoimitus:
     def __init__(self, sovelluslogiikka, _lue_syote):
        self.sovelluslogiikka=sovelluslogiikka
        self._luku=_lue_syote

     def suorita(self):
        syote = self._luku()
        global EDELLINEN_LUKU
        EDELLINEN_LUKU=syote
        return self._suorita_lasku(syote)

class Summa(Laskutoimitus):
    def __init__(self, sovelluslogiikka, _lue_syote):
        super().__init__(sovelluslogiikka, _lue_syote)
 
    def _suorita_lasku(self, syote): 
        self.sovelluslogiikka.plus(int(syote))

class Erotus(Laskutoimitus):
    def __init__(self, sovelluslogiikka, _lue_syote):
        super().__init__(sovelluslogiikka, _lue_syote)
 
    def _suorita_lasku(self, syote):
        self.sovelluslogiikka.miinus(int(syote))

class Nollaus(Laskutoimitus):
    def __init__(self, sovelluslogiikka, _lue_syote=None):
        super().__init__(sovelluslogiikka, _lue_syote)
 
    def suorita(self): 
        self.sovelluslogiikka.nollaa()

class Kumoa(Laskutoimitus):
    def __init__(self, sovelluslogiikka, _lue_syote):
        super().__init__(sovelluslogiikka, _lue_syote)
 
    def suorita(self): 
        self.sovelluslogiikka.kumoa(EDELLINEN_LUKU)