import unittest

from src.lab2.rsa import gcd, generate_keypair, is_prime, multiplicative_inverse


class IsPrimeTestCase(unittest.TestCase):
    def test_primes(self):
        for number in (2, 3, 5, 11, 97, 7919):
            with self.subTest(number=number):
                self.assertTrue(is_prime(number))

    def test_not_primes(self):
        for number in (-7, 0, 1, 4, 8, 9, 100, 7917):
            with self.subTest(number=number):
                self.assertFalse(is_prime(number))


class GcdTestCase(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(3, 7), 1)
        self.assertEqual(gcd(48, 18), 6)

    def test_gcd_with_zero_and_order(self):
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(21, 14), gcd(14, 21))


class MultiplicativeInverseTestCase(unittest.TestCase):
    def test_known_value(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)

    def test_inverse_property(self):
        phi = 3120
        for e_value in (7, 17, 101, 2753):
            with self.subTest(e=e_value):
                d_value = multiplicative_inverse(e_value, phi)
                self.assertEqual(d_value * e_value % phi, 1)

    def test_not_coprime(self):
        with self.assertRaises(ValueError):
            multiplicative_inverse(4, 40)


class GenerateKeypairTestCase(unittest.TestCase):
    def test_invalid_numbers(self):
        with self.assertRaises(ValueError):
            generate_keypair(4, 7)
        with self.assertRaises(ValueError):
            generate_keypair(7, 7)

    def test_keys_are_consistent(self):
        p_value, q_value = 61, 53
        phi = (p_value - 1) * (q_value - 1)
        for _ in range(20):
            (e_value, n_value), (d_value, n_private) = generate_keypair(p_value, q_value)
            self.assertEqual(n_value, p_value * q_value)
            self.assertEqual(n_private, n_value)
            self.assertEqual(gcd(e_value, phi), 1)
            self.assertEqual(d_value * e_value % phi, 1)

    def test_encrypt_decrypt_with_generated_keys(self):
        public, private = generate_keypair(61, 53)
        for char in "Hello, RSA!":
            with self.subTest(char=char):
                encrypted = pow(ord(char), public[0], public[1])
                self.assertEqual(chr(pow(encrypted, private[0], private[1])), char)


if __name__ == "__main__":
    unittest.main()