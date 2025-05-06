import string
import random
import argparse


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
        "--count", "-c", type=int, help="The number of passwords to be generated.",default=1
    )

    args = parser.parse_args()
    for i in range(args.count):
        password = Password.generate(
        length=args.length,
        upper_case=args.upper_case,
        lower_case=args.lower_case,
        special_char=args.special_char,
        digits=args.digits,
        )
        print(password)
