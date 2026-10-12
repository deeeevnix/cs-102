"""Шифр Цезаря."""


def shift_char(char: str, shift: int) -> str:
    """Сдвигает латинскую букву на shift позиций с сохранением регистра, остальные символы не меняет."""
    if "a" <= char <= "z":
        base = ord("a")
    elif "A" <= char <= "Z":
        base = ord("A")
    else:
        return char
    return chr((ord(char) - base + shift) % 26 + base)


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for char in plaintext:
        ciphertext += shift_char(char, shift)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for char in ciphertext:
        plaintext += shift_char(char, -shift)
    return plaintext
