import string
import random

class Password:
    @staticmethod
    def generate(length = 8):
        """
        Generate a random password of specified length.

        Args:
            length (int): Length of the password. Default is 8.

        Returns:
            str: A randomly generated password.
        """
        if not isinstance(length, int) or length <= 0:
            raise ValueError("Password length must be a positive integer.")
        characters = string.ascii_letters + string.punctuation + string.digits
        return ''.join(random.choices(characters, k=length))
