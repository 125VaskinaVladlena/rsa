import random
import math

PRIMES = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107  
]
PRIMES = [p for p in PRIMES if p <= 106]

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a: int, b: int):
    """Расширенный алгоритм Евклида, возвращает (g, x, y) такие что a*x + b*y = g = gcd(a,b)"""
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def mod_inverse(e: int, phi: int) -> int:
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise Exception('Обратного элемента не существует')
    return x % phi

def is_prime(n: int) -> bool:
    return n in PRIMES

def generate_keypair() -> tuple:
    p = random.choice(PRIMES)
    q = random.choice(PRIMES)
    while q == p:
        q = random.choice(PRIMES)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.choice([prime for prime in PRIMES if 1 < prime < phi and gcd(prime, phi) == 1])

    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(public_key: tuple, plaintext: int) -> int:
    e, n = public_key
    if not (0 <= plaintext < n):
        raise ValueError(f'Текст должен быть в диапазоне [0, {n-1}]')
    return pow(plaintext, e, n)

def decrypt(private_key: tuple, ciphertext: int) -> int:
    d, n = private_key
    return pow(ciphertext, d, n)

if __name__ == '__main__':
    public_key, private_key = generate_keypair()
    print("Публичный ключ:", public_key)
    print("Приватный ключ:", private_key)

    message = 42 
    print("Исходное сообщение:", message)

    encrypted = encrypt(public_key, message)
    print("Зашифрованное сообщение:", encrypted)

    decrypted = decrypt(private_key, encrypted)
    print("Расшифрованное сообщение:", decrypted)