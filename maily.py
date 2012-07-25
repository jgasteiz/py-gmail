#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import json
import smtplib
import argparse
import mimetypes
from email import encoders
from optparse import OptionParser
from email.message import Message
from email.mime.text import MIMEText

__author__ = 'Javi Manzano | https://github.com/jgasteiz'
__license__ = 'GPL'
__version__ = '0.1'
__email__ = 'javi.manzano.oller@gmail.com'

def main():
    """
    Description
    -----------
    This script will send email from a gmail account

    Gmail authentication must be specified in a json settings file

    Parameters
    ----------
    -m, --message : string, the message you want to send
        Must
    -s, --subject : string, message subject
        Must
    -d, --destination : string, destination address
        Must

    Examples
    --------
    python maily.py -m 'Hello, World!' -s 'Test' -d 'javi.manzano.oller@gmail.com'

    """

    # ArgumentParser
    parser = argparse.ArgumentParser(
        description='Minifies js code using google closure.')
    parser.add_argument('-m', '--message',
                        help='Message you want to send',
                        required=True)
    parser.add_argument('-s', '--subject',
                        help='Email subject',
                        required=True)
    parser.add_argument('-d', '--destination',
                        help='Destination email',
                        required=True)

    ARGS = vars(parser.parse_args())
    message = ARGS['message']
    subject = ARGS['subject']
    destination = ARGS['destination']

    # You should put this settings file in a secure place
    settings_file = open('my-settings.json')
    settings = json.load(settings_file)
    origin = settings['origin']
    password = settings['password']
    settings_file.close()

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['From'] = origin
    msg['Reply-to'] = origin
    msg['To'] = destination

    sender = smtplib.SMTP('smtp.gmail.com')
    sender.ehlo()
    sender.starttls()
    sender.login(origin, password)
    sender.sendmail(origin, destination, msg.as_string())
    sender.close()

if __name__ == "__main__":
    main()