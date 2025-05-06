# MyPassMaker

**MyPassMaker** is a simple and secure password generator that can create both random passwords and memorable passphrases.

[![Downloads](https://pepy.tech/badge/mypassmaker)](https://pepy.tech/project/mypassmaker)  
[![GitHub stars](https://img.shields.io/github/stars/edrisranjbar/mypassmaker?style=social)](https://github.com/edrisranjbar/mypassmaker/stargazers)

## Features

- Generate random passwords with customizable length and character sets
- Generate memorable passphrases using a wordlist
- Password safety evaluation
- Command-line interface with various options

## Installation

Install the package via pip:

```bash
pip install mypassmaker
```

## Usage

### Generate Random Passwords

```bash
python -m mypassmaker [options]
```

Options for random password generation:
- `--length` or `-len`: Password length (default: 8)
- `--upper_case` or `-u`: Include uppercase letters
- `--lower_case` or `-l`: Include lowercase letters
- `--special_char` or `-s`: Include special characters
- `--digits` or `-d`: Include digits
- `--count` or `-c`: Number of passwords to generate (default: 1)

Example:
```bash
python -m mypassmaker --length 12 --upper_case --lower_case --special_char --digits
```

### Generate Passphrases

```bash
python -m mypassmaker --passphrase [options]
```

Options for passphrase generation:
- `--words` or `-w`: Number of words in passphrase (default: 4)
- `--separator` or `-sep`: Character to separate words (default: '-')
- `--count` or `-c`: Number of passphrases to generate (default: 1)

Example:
```bash
python -m mypassmaker --passphrase --words 4 --separator "-"
```

This will generate passphrases like "correct-horse-battery-staple" using words from the built-in wordlist.

## Password Safety

The tool includes a safety evaluation feature that checks:
- Password length (>= 8)
- Presence in common password lists
- Use of special characters
- Mix of uppercase and lowercase letters
- Inclusion of numbers

## License

MIT License

## How to Contribute
We appreciate your interest in contributing to MyPassMaker! Here's how you can help:

1. Fork the repository.
2. Make your changes or add new features.
3. Write tests to ensure your changes work as expected.
4. Submit a Pull Request (PR) with a description of your changes.

We'll review your PR and merge it if it aligns with the project goals.

## Contact Us

We'd love to hear from you! Whether you have feedback, suggestions, or questions, feel free to reach out:

- **Email**: [edris.qeshm2@gmail.com](mailto:edris.qeshm2@gmail.com)  
- **Website**: [www.edrisranjbar.ir](http://www.edrisranjbar.ir)  
- **LinkedIn**: [Edris Ranjbar](https://www.linkedin.com/in/edris-ranjbar/)  
- **GitHub**: [MyPassMaker Repository](https://github.com/edrisranjbar/mypassmaker)

Stay connected and help us make **MyPassMaker** even better!
