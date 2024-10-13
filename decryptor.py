import argparse

parser = argparse.ArgumentParser(description="Decrypting ROT")
parser.add_argument("-r", "--rotation", type=int, required=True, help="Set rotation")
parser.add_argument("-a", "--alphabet", required=True, help="Set alphabet")
parser.add_argument("-e", "--encrypted", required=True, help="Encrypted text")

args = parser.parse_args()

alphabet = [str(i) for i in args.alphabet]
table_of_switches = {}


def find(symb: str) -> int:
    for i in range(0, len(alphabet)):
        if alphabet[i] == symb:
            return i


def encrypt_char(symb: str) -> str:
    return alphabet[(find(symb) + args.rotation) % len(alphabet)]


def fill():
    for i in alphabet:
        table_of_switches[encrypt_char(i)] = i


def decrypt() -> str:
    fill()
    ans = ""
    for i in args.encrypted:
        ans += table_of_switches[i]
    return ans


if __name__ == "__main__":
    print(decrypt())