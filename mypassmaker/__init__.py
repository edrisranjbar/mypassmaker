class Password:
    @staticmethod
    def generate(length = 8):
        import string
        import random
        char = string.ascii_letters + string.punctuation + string.digits
        final_password = "".join(random.choice(char) for x in range(int(length)))
        return final_password

    @staticmethod
    def send_email(gmail_user, gmail_password, sent_from, send_to, content):
        try:
            import smtplib
        except ImportError:
            raise Exception("Please first install smtplib via: pip install smtplib")
        subject = "Here's Your Secure password"
        print(content)

        email_text = "From: {}\nTo: {}\nSubject: {}\n\n This is your password: {}".format(sent_from, send_to, subject, content)
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, send_to, email_text)
            server.close()
            return True
        except smtplib.SMTPAuthenticationError:
            return False
        except smtplib.SMTPConnectError:
            return False
