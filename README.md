# MyPassMaker
*mypassmaker* is a python package for making strong password and check passwords.

## How yo use?
```python
from mypassmaker import Password
```
```python
my_password = Password.generate(length=10)
```
and if you wanna have your password in your gmail inbox, then you can use ```send_email()``` method like this:
```python
Password.send_email(gmail_user="", gmail_password="", sent_from="", send_to="", my_password=my_password)
```

## How to contribute?
Thanks for being so kind about this project. It is completely Open Shource so go ahead and make a **Fork** for yourself and work on it. When you are ready; You can just make a Pull Request (PR) and I will commit your changes if it is possible.

## Contact Us
E-mail: edris.qeshm2@gmail.com
<br>
Website: www.edrisranjbar.ir