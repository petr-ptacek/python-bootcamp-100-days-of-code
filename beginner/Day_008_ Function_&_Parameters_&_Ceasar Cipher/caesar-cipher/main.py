from aplhabet import alphabet
from art import logo


def get_position(letter: str, shift_amount: int):
    position = alphabet.index(letter)

    if position + shift_amount >= len(alphabet):
        return (position + shift_amount) - len(alphabet)
    elif position + shift_amount < 0:
        return len(alphabet) + (position + shift_amount)
    else:
        return position + shift_amount


def encrypt(plain_text: str, shift_amount: int):
    cipher_text = ""

    for letter in plain_text:
        new_position = get_position(letter, shift_amount)
        print(f"new_position: {new_position}")
        new_letter = alphabet[new_position]
        cipher_text += new_letter

    print(f"The encoded text is {cipher_text}")
    return cipher_text


def decrypt(cipher_text: str, shift_amount: int):
    plain_text = ""

    for letter in cipher_text:
        new_position = get_position(letter, shift_amount * -1)
        print(f"new_position: {new_position}")
        plain_text += alphabet[new_position]

    print(f"The decoded text is {plain_text}")
    return plain_text


def caesar(start_text: str, shift_amount: int, cipher_direction: str):
    end_text = ""

    for char in start_text:
        if char not in alphabet:
            end_text += char
            continue

        position = get_position(char, shift_amount)
        if cipher_direction == "decode":
            position = get_position(char, shift_amount * -1)

        end_text += alphabet[position]

    print(f"The {cipher_direction}d text is {end_text}")


def main():
    print(logo)
    should_continue = True

    while should_continue:
        direction = input("> Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("> Type your message:\n").lower()
        shift = int(input("> Type the shift number:\n")) % len(alphabet)

        caesar(start_text=text, cipher_direction=direction, shift_amount=shift)
        should_continue = input("> Type 'yes' if you want to go again. Otherwise type 'no'\n").lower() == "yes"


main()
