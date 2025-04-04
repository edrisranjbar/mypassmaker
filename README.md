# MyPassMaker

**MyPassMaker** is a Python package designed to help you generate strong passwords and assess their safety.

[![Downloads](https://pepy.tech/badge/mypassmaker)](https://pepy.tech/project/mypassmaker)  
[![GitHub stars](https://img.shields.io/github/stars/edrisranjbar/mypassmaker?style=social)](https://github.com/edrisranjbar/mypassmaker/stargazers)

---

## Features
- Generate strong, secure passwords.
- Lightweight and easy to use.
- Test your password's safety level.
---

## Installation

Install the package via pip:

```bash
pip install mypassmaker
```

## How to Use
Generate a secure password of a specified length:

```python
from mypassmaker import Password

# Generate a 10-character password
my_password = Password.generate(length=10)
print(my_password)
```

### Checking Password Safety
The check_safety() method evaluates the safety of a password based on various criteria and returns a score between 0 and 10. The following criteria are checked:

- Length (>= 8)
- Not in the passlist (stored in passlist.txt)
- Contains special characters
- Contains both uppercase and lowercase letters
- Contains numbers (and not a number-only password)

```python
from mypassmaker import Password

password = "A1!strongPass"
safety_score = Password.check_safety(password)

print(f"Password Safety Score: {safety_score}/10")
```

### Example Scoring
- 10: Perfect password with length, complexity, and variety.
- 5: A password that meets some but not all safety criteria.
- 0: A weak password that fails several checks.

## How to Contribute
We appreciate your interest in contributing to MyPassMaker! Here's how you can help:

1. Fork the repository.
2. Make your changes or add new features.
3. Write tests to ensure your changes work as expected.
4. Submit a Pull Request (PR) with a description of your changes.

We’ll review your PR and merge it if it aligns with the project goals.

## Contact Us

We’d love to hear from you! Whether you have feedback, suggestions, or questions, feel free to reach out:

- **Email**: [edris.qeshm2@gmail.com](mailto:edris.qeshm2@gmail.com)  
- **Website**: [www.edrisranjbar.ir](http://www.edrisranjbar.ir)  
- **LinkedIn**: [Edris Ranjbar](https://www.linkedin.com/in/edris-ranjbar/)  
- **GitHub**: [MyPassMaker Repository](https://github.com/edrisranjbar/mypassmaker)

Stay connected and help us make **MyPassMaker** even better!
