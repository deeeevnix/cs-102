import unittest
from src.lab2.caesar import decrypt_caesar, encrypt_caesar

class CaesarTestCase(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(encrypt_caesar('python'), 'sbwkrq')
        self.assertEqual(encrypt_caesar("PYTHON"), "SBWKRQ")
        self.assertEqual(encrypt_caesar("Hello", 5), "Mjqqt")

    def test_decrypt(self):
        self.assertEqual(decrypt_caesar("SBWKRQ"), "PYTHON")
        self.assertEqual(decrypt_caesar("Mjqqt", 5), "Hello")

    def test_alphabet_wraps_arround(self):
        self.assertEqual(encrypt_caesar("XYZ xyz"), "ABC abc")

    def test_non_letters_unchanged(self):
        self.assertEqual(encrypt_caesar("Python 3.8!"), "Sbwkrq 3.8!")

    def test_zero_shift_and_empty_string(self):
        self.assertEqual(encrypt_caesar("Hello, World!", 0), "Hello, World!")
        self.assertEqual(encrypt_caesar(""), "")

    def test_round_trip(self):
        text = "Hello, World! Python 3.6"
        for shift in (-30, -1, 0, 3, 13, 26, 100):
            with self.subTest(shift=shift):
                self.assertEqual(decrypt_caesar(encrypt_caesar(text, shift), shift), text)

if __name__ == "__main__":
    unittest.main()



    
        