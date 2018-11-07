#!/usr/bin/python
# -*- coding: UTF-8 -*-
import send_email

s = send_email.Send_email()

from_addr = input("Your email:")
from_name = input("Your name:")
to_addr = input("Receiver's email:")
to_name = input("Receiver's name:")
password = input("Your password:")
smtp_server = input("SMTP:")
subject = input("Subject:")
message = input("Text:")

s.set_details(from_addr, password, to_addr, smtp_server, from_name, to_name, message, subject)
s.login_and_send()