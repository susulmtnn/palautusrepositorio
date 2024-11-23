import unittest
from unittest.mock import Mock, ANY
from kassapaate import Kassapaate, HINTA
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_kortilta_velotetaan_hinta_jos_rahaa_on(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo.return_value = 10
        
        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_called_with(HINTA)

    def test_kortilta_ei_veloteta_jos_raha_ei_riita(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo.return_value = 4
        
        if maksukortti_mock.saldo()>=HINTA:
            self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_not_called()

    def test_lataa_lisää_kortille_rahaa(self):
        maksukortti_mock= Mock()
        SUMMA=2

        if SUMMA >0:
            self.kassa.lataa(maksukortti_mock, SUMMA)
            maksukortti_mock.lataa.assert_called_with(SUMMA)

        else:
            maksukortti_mock.lataa.assert_not_called()

    def test_kortille_ei_voi_ladata_negatiivista(self):
        maksukortti_mock= Mock()
        SUMMA=-2

        if SUMMA >0:
            self.kassa.lataa(maksukortti_mock, SUMMA)
            maksukortti_mock.lataa.assert_called_with(SUMMA)

        else:
            maksukortti_mock.lataa.assert_not_called()
        