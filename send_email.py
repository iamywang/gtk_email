#!/usr/bin/python
# -*- coding: UTF-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


class Send_email:
    from_addr = to_addr = ""
    password = smtp_server = ""
    msg = ""

    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def set_details(self, from_addr, password, to_addr, smtp_server, from_name, to_name, message, subject):
        self.from_addr = from_addr
        self.password = password
        self.to_addr = to_addr
        self.smtp_server = smtp_server

        msg = MIMEText(message, 'plain', 'utf-8')
        msg['From'] = self._format_addr((from_name + ' <%s>') % self.from_addr)
        msg['To'] = self._format_addr((to_name + ' <%s>') % self.to_addr)
        msg['Subject'] = Header(subject, 'utf-8').encode()

        self.msg = msg

    def login_and_send(self):
        server = smtplib.SMTP(self.smtp_server, 25)
        server.set_debuglevel(1)
        server.login(self.from_addr, self.password)
        server.sendmail(self.from_addr, [self.to_addr], self.msg.as_string())
        server.quit()
