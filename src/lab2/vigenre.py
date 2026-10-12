"""Шифр Виженера."""


def is_latin_letter(char: str) -> bool:
    """Проверяет, что символ является латинской буквой."""
    return "a" <= char.lower() <= "z" and char.isascii()


def shift_char(char: str, shift: int) -> str:
    """Сдвигает латинскую букву на shift позиций с сохранением регистра, остальные символы не меняет."""
    if not is_latin_letter(char):
        return char
    base = ord("a") if char.islower() else ord("A")
    return chr((ord(char) - base + shift) % 26 + base)


def key_shift(keyword: str, index: int) -> int:
    """Возвращает сдвиг, который задаёт символ ключа с номером index (ключ повторяется по кругу)."""
    return ord(keyword[index % len(keyword)].lower()) - ord("a")


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    if not keyword:
        return plaintext
    key_index = 0
    for char in plaintext:
        if is_latin_letter(char):
            ciphertext += shift_char(char, key_shift(keyword, key_index))
            key_index += 1
        else:
            ciphertext += char
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    if not keyword:
        return ciphertext
    key_index = 0
    for char in ciphertext:
        if is_latin_letter(char):
            plaintext += shift_char(char, -key_shift(keyword, key_index))
            key_index += 1
        else:
            plaintext += char
    return plaintext
