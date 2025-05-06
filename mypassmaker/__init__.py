import string
import random
import argparse
import os
import json
import csv
from typing import List, Union


class Password:
    @staticmethod
    def generate(
        length: int = 8,
        upper_case: bool = True,
        lower_case: bool = True,
        special_char: bool = True,
        digits: bool = True,
    ):
        """
        Generate a random password of specified length.

        Args:
            length (int): Length of the password. Default is 8.

        Returns:
            str: A randomly generated password.
        """
        if not isinstance(length, int) or length <= 0:
            raise ValueError("Password length must be a positive integer.")
        characters = ""
        if upper_case:
            characters += string.ascii_uppercase
        if lower_case:
            characters += string.ascii_lowercase
        if special_char:
            characters += string.punctuation
        if digits:
            characters += string.digits
        return "".join(random.choices(characters, k=length))

    @staticmethod
    def generate_passphrase(length: int = 4, separator: str = "-"):
        """
        Generate a memorable passphrase using words from the wordlist.

        Args:
            length (int): Number of words in the passphrase. Default is 4.
            separator (str): Character to separate words. Default is '-'.

        Returns:
            str: A randomly generated passphrase.
        """
        if not isinstance(length, int) or length <= 0:
            raise ValueError("Passphrase length must be a positive integer.")

        wordlist_path = os.path.join(os.path.dirname(__file__), "wordlist.txt")
        try:
            with open(wordlist_path, "r") as file:
                wordlist = [word.strip() for word in file.readlines()]
        except FileNotFoundError:
            raise FileNotFoundError("Wordlist file not found. Please ensure wordlist.txt exists.")

        if not wordlist:
            raise ValueError("Wordlist is empty.")

        words = random.choices(wordlist, k=length)
        return separator.join(words)

    @staticmethod
    def check_safety(password):
        """
        Evaluates the safety of a password based on multiple criteria:
        - Length (>= 8)
        - Not in the passlist (passlist.txt)
        - Contains special characters
        - Contains both uppercase and lowercase characters
        - Contains numbers (not a number-only password)

        Returns a safety score (0-10).
        """
        safety_level = 0

        # 1. Check password length (>= 8)
        if len(password) >= 8:
            safety_level += 2

        # 2. Check if password is not in the passlist
        try:
            with open("passlist.txt", "r") as file:
                pass_list = set(file.read().splitlines())
        except FileNotFoundError:
            pass_list = set()

        if password not in pass_list:
            safety_level += 2

        # 3. Check for special characters
        special_characters = set("!@#$%^&*()_+=/,<>;:")
        if any(character in special_characters for character in password):
            safety_level += 2

        # 4. Check for both uppercase and lowercase letters
        if any(character.isupper() for character in password) and any(
            character.islower() for character in password
        ):
            safety_level += 2

        # 5. Check for at least one number and ensure password isn't numeric only
        if (
            any(character.isdigit() for character in password)
            and not password.isdigit()
        ):
            safety_level += 2

        return safety_level

    @staticmethod
    def save_to_file(passwords: List[str], output_file: str, format: str = "txt"):
        """
        Save generated passwords to a file in the specified format.

        Args:
            passwords (List[str]): List of passwords to save
            output_file (str): Path to the output file
            format (str): Output format ('txt', 'json', or 'csv')
        """
        if not passwords:
            raise ValueError("No passwords to save")

        os.makedirs(os.path.dirname(output_file) or ".", exist_ok=True)

        if format == "txt":
            with open(output_file, "w") as f:
                f.write("\n".join(passwords))
        elif format == "json":
            with open(output_file, "w") as f:
                json.dump({"passwords": passwords}, f, indent=2)
        elif format == "csv":
            with open(output_file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["password"])
                for password in passwords:
                    writer.writerow([password])
        else:
            raise ValueError(f"Unsupported format: {format}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A Strong password generator")
    parser.add_argument(
        "--length", "-len", type=int, help="length of password", default=8
    )
    parser.add_argument(
        "--upper_case", "-u", action="store_true", help="use upper case in password"
    )
    parser.add_argument(
        "--lower_case", "-l", action="store_true", help="use lower_case in password"
    )
    parser.add_argument(
        "--special_char", "-s", action="store_true", help="use special_char in password"
    )
    parser.add_argument(
        "--digits", "-d", action="store_true", help="use digits in password"
    )
    parser.add_argument(
        "--count", "-c", type=int, help="The number of passwords to be generated.", default=1
    )
    parser.add_argument(
        "--passphrase", "-p", action="store_true", help="Generate a passphrase instead of a random password"
    )
    parser.add_argument(
        "--words", "-w", type=int, help="Number of words in passphrase", default=4
    )
    parser.add_argument(
        "--separator", "-sep", type=str, help="Separator character for passphrase words", default="-"
    )
    parser.add_argument(
        "--output", "-o", type=str, help="Output file to save passwords"
    )
    parser.add_argument(
        "--format", "-f", type=str, choices=["txt", "json", "csv"], default="txt",
        help="Output format (txt, json, or csv)"
    )

    args = parser.parse_args()
    if args.count < 1:
        parser.error("--count must be a positive integer (>= 1)")
    
    passwords = []
    for i in range(args.count):
        if args.passphrase:
            password = Password.generate_passphrase(length=args.words, separator=args.separator)
        else:
            password = Password.generate(
                length=args.length,
                upper_case=args.upper_case,
                lower_case=args.lower_case,
                special_char=args.special_char,
                digits=args.digits,
            )
        passwords.append(password)
        print(password)

    if args.output:
        try:
            Password.save_to_file(passwords, args.output, args.format)
            print(f"\nPasswords saved to {args.output} in {args.format} format")
        except Exception as e:
            print(f"Error saving passwords: {e}")
