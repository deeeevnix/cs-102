import unittest

from src.lab2.vigenre import decrypt_vigenere, encrypt_vigenere

class VigenreTestCase(unittest.TestCase):
    def test_encrypt_know_example(self):
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")

    def test_decrypt_know_example(self):
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), "ATTACKATDAWN")

    def test_key_a_does_not_change_text(self):
        self.assertEqual(encrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(decrypt_vigenere("python", "a"), "python")

    def test_key_case_is_ignored(self):
        self.assertEqual(encrypt_vigenere("ATTACK", "lemon"), encrypt_vigenere("ATTACK", "LEMON"))

    def test_non_letters_do_not_use_key(self):
        self.assertEqual(encrypt_vigenere("A T!", "BC"), "B V!")

    def test_round_trip(self):
        text = "Hello, World! Attack at dawn."
        for key in ("a", "key", "LEMON", "longerkeythanthetext" * 3):
            with self.subTest(key=key):
                self.assertEqual(decrypt_vigenere(encrypt_vigenere(text, key), key), text)

    def test_empty_key_and_text(self):
        self.assertEqual(encrypt_vigenere("Hello", ""), "Hello")
        self.assertEqual(decrypt_vigenere("", "key"), "")

if __name__ == '__main__':
    unittest.main()
