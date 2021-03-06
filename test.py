# Will use codecs, as 'str' object in Python 3 doesn't have any attribute 'decode'
import unittest
import rc4

class TestMethods(unittest.TestCase):

    def test_rc4(self):

        key = b'not-so-random-key'  # byte-string
        plaintext = b'Good work! Your implementation is correct'  # byte-string

        ciphertext = rc4.encrypt(key, plaintext)
        decrypted = rc4.encrypt(key, ciphertext)

        self.assertEqual(plaintext, decrypted)



