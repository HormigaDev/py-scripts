import string
import secrets
import argparse

def generate_password(length: int, complexity: int) -> str:
    characters = string.ascii_lowercase

    if complexity >= 4:
        characters += string.ascii_uppercase
    if complexity >= 6:
        characters += string.digits
    if complexity >= 8:
        characters += string.punctuation

    return ''.join(secrets.choice(characters) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(description="Genera una contraseña aleatoria y segura.")
    parser.add_argument('--length', type=int, required=True, help="Longitud de la contraseña")
    parser.add_argument('--complexity', type=int, required=True, help="Nivel de complejidad de la contraseña (1-10)")
    args = parser.parse_args()

    password = generate_password(args.length, args.complexity)
    print(password)

main()