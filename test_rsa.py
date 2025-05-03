import unittest
import rsa

class TestRSA(unittest.TestCase):

    def test_keypair_generation(self):
        public_key, private_key = rsa.generate_keypair()
        e, n_pub = public_key
        d, n_priv = private_key
        self.assertEqual(n_pub, n_priv, "Модули открытого и закрытого ключей должны совпадать")
        self.assertTrue(rsa.is_prime(e) or e < n_pub, "e должно быть допустимым числом")

        phi = None
        try:
            _ = rsa.mod_inverse(e, (n_pub // e) * (n_pub // (n_pub // e) - 1))
        except Exception:
            pass

    def test_encryption_decryption(self):
        public_key, private_key = rsa.generate_keypair()
        n = public_key[1]
        for message in [0, 1, 42, n - 1]:  
            with self.subTest(message=message):
                encrypted = rsa.encrypt(public_key, message)
                decrypted = rsa.decrypt(private_key, encrypted)
                self.assertEqual(message, decrypted, "Расшифрованное сообщение должно совпадать с исходным")

    def test_invalid_message(self):
        public_key, _ = rsa.generate_keypair()
        n = public_key[1]
        with self.assertRaises(ValueError):
            rsa.encrypt(public_key, n)
            def test_mod_inverse(self):
                for a, m in [(3, 11), (10, 17), (7, 40)]:
                    inv = rsa.mod_inverse(a, m)
                    self.assertEqual((a * inv) % m, 1, "Обратный элемент должен удовлетворять (a * inv) mod m = 1")

if __name__ == '__main__':
    unittest.main()