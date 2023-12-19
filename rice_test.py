import unittest
from unittest.mock import patch
from io import StringIO
from rice import choisir_mode

class TestRiceCooker(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '1'])
    def test_mode_riz_blanc(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            choisir_mode()
        expected_output = 'Mode Riz Blanc sélectionné\nLa cuisson se déroulera pendant 2 secondes.\n*BIP*BIP*BIP* La cuisson est terminée !\nQue voulez-vous faire maintenant? (1. Éteindre / 2. Maintenir au chaud) : Le rice cooker a été éteint.'
        self.assertIn(expected_output, mock_stdout.getvalue().strip())

    @patch('builtins.input', side_effect=['4', '0', '1'])
    def test_mode_autre_aliment_temps_invalide(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            choisir_mode()
        expected_output = 'Mode Autre Aliment sélectionné - Cuisson pendant 0 secondes.\nTemps invalide.\nQue voulez-vous faire maintenant? (1. Éteindre / 2. Maintenir au chaud) : Choix non valide. Le rice cooker sera éteint par défaut.'
        self.assertIn(expected_output, mock_stdout.getvalue().strip())

    @patch('builtins.input', side_effect=['5', '1'])
    def test_choix_non_valide(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            choisir_mode()
        expected_output = 'Choix non valide'
        self.assertIn(expected_output, mock_stdout.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
