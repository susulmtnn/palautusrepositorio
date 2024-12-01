KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
            self.kapasiteetti=self.aseta_kapasiteetti(kapasiteetti)
            self.kasvatuskoko= self.aseta_kasvatuskoko(kasvatuskoko, kapasiteetti)
            self.ljono = self._luo_lista(self.kapasiteetti)
            self.alkioiden_lkm = 0

    def aseta_kasvatuskoko(self, kasvatuskoko, kapasiteetti):
         if kasvatuskoko is None:
            return OLETUSKASVATUS
         elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kasvatuskokovirhe: Annettu kapasiteetti joko ei ole luku, tai on negatiivinen")  # heitin vaan jotain :D
         else:
            return kasvatuskoko

    def aseta_kapasiteetti(self, kapasiteetti):
        if kapasiteetti is None:
            return KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteettivirhe: Annettu kapasiteetti joko ei ole luku, tai on negatiivinen")  # heitin vaan jotain :D
        else:
            return kapasiteetti

    def kuuluu(self, luku):
        #olisin halunnut muuttaa metodin nimeä, mutta en ollut varma saanko koskea testeihin.
        if luku in self.ljono:
            return True
        else:
            return False
        
    def lisaa_eka_luku(self, n):
            self.ljono[self.alkioiden_lkm]=n
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True
    
    def luo_uusi_sailytyspaikka(self):
            vanha_ljono = self.ljono
            self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_lista(vanha_ljono, self.ljono)
            return True

    def lisaa(self, n):
        if self.alkioiden_lkm == 0 or not self.kuuluu(n):
            self.lisaa_eka_luku(n)
            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm == len(self.ljono):
                self.luo_uusi_sailytyspaikka()
        return False

    def poista(self, n):
        if n in self.ljono:
            self.ljono.remove(n)
            self.alkioiden_lkm-=1
            return True
        return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        int_list = self._luo_lista(self.alkioiden_lkm)
        for i in range(0, len(int_list)):
            int_list[i] = self.ljono[i]
        return int_list

    @staticmethod
    def luo_instanssi(a, b):
        a_lista = a.to_int_list()
        b_lista = b.to_int_list()
        return a_lista, b_lista


    @staticmethod
    def yhdiste(a, b):
        joukko = IntJoukko()
        a_lista, b_lista = joukko.luo_instanssi(a, b)
        for i in range(0, len(a_lista)):
            joukko.lisaa(a_lista[i])
        for i in range(0, len(b_lista)):
            joukko.lisaa(b_lista[i])
        return joukko

    @staticmethod
    def leikkaus(a, b):
        joukko = IntJoukko()
        a_lista, b_lista = joukko.luo_instanssi(a, b)
        for i in range(0, len(a_lista)):
            for j in range(0, len(b_lista)):
                if a_lista[i] == b_lista[j]:
                    joukko.lisaa(b_lista[j])
        return joukko

    @staticmethod
    def erotus(a, b):
       joukko = IntJoukko()
       a_lista, b_lista = joukko.luo_instanssi(a, b)
       for i in range(0, len(a_lista)):
            joukko.lisaa(a_lista[i])
       for i in range(0, len(b_lista)):
            joukko.poista(b_lista[i])
       return joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        while self.ljono[-1]==0:
            self.ljono.pop()
            self.alkioiden_lkm-=1
        else:
            return "{" + ", ".join(map(str, self.ljono)) + "}"
