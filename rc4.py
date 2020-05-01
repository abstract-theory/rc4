# Will use codecs, as 'str' object in Python 3 doesn't have any attribute 'decode'

MOD = 256

def KSA(key):
    ''' Key Scheduling Algorithm (from wikipedia):
        for i from 0 to 255
            S[i] := i
        endfor
        j := 0
        for i from 0 to 255
            j := (j + S[i] + key[i mod keylength]) mod 256
            swap values of S[i] and S[j]
        endfor
    '''
    key_length = len(key)
    # create the array "S"
    S = list(range(MOD))  # [0,1,2, ... , 255]
    j = 0
    for i in range(MOD):
        j = (j + S[i] + key[i % key_length]) % MOD
        S[i], S[j] = S[j], S[i]  # swap values

    return S


def PRGA(S):
    ''' Psudo Random Generation Algorithm (from wikipedia):
        i := 0
        j := 0
        while GeneratingOutput:
            i := (i + 1) mod 256
            j := (j + S[i]) mod 256
            swap values of S[i] and S[j]
            K := S[(S[i] + S[j]) mod 256]
            output K
        endwhile
    '''
    i = 0
    j = 0
    while True:
        i = (i + 1) % MOD
        j = (j + S[i]) % MOD

        S[i], S[j] = S[j], S[i]  # swap values
        K = S[(S[i] + S[j]) % MOD]
        yield K


def encrypt(key, plaintext):
    '''
    args
        key: Encryption key as a string. Characters may occupy full
        8-bit range.

        plaintext: Plaintext to encrypt. Character may occupy full 8-bit
        range.

    return
        res: Encrypted text as string.
    '''
    plaintext = [ord(c) for c in plaintext]
    key = [ord(c) for c in key]
    keystream = PRGA(KSA(key))
    dec = [chr(c^next(keystream)) for c in plaintext]
    res = ''.join(dec)
    return res


def demo():

    key = 'not-so-random-key'  # plaintext
    plaintext = 'Good work! Your implementation is correct'  # plaintext

    ciphertext = encrypt(key, plaintext) # encrypt
    decrypted = encrypt(key, ciphertext) # decrypt

    print('plaintext:', plaintext)
    print('ciphertext:', ciphertext)
    print('decrypted:', decrypted)

    if plaintext == decrypted:
        print('\nCongrats ! You made it.')
    else:
        print('\nOh no! Something went wrong!')


if __name__ == "__main__":
    demo()
