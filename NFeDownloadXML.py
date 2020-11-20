# Something in lines of http://stackoverflow.com/questions/348630/how-can-i-download-all-emails-with-attachments-from-gmail
# Make sure you have IMAP enabled in your gmail settings.
# Right now it won't download same file name twice even if their contents are different.

import email
import getpass, imaplib
import os
import sys

import dnlconfig as cfg

userName = cfg.server["EMAIL"]
passwd = cfg.server["PWD"]

def main():

    imap = imaplib.IMAP4_SSL(cfg.server["IMAP"])
    imap.login(userName, passwd)
    boxList = imap.list()

    # print(boxList)

    imap.select('INBOX')

    # imap.select(readonly=False) # so we can mark mails as read
    status, response = imap.search(None, '(UNSEEN)')
    unread_msg_nums = response[0].split()

    print(len(unread_msg_nums))

    # Iterating over all emails
    for msgId in response[0].split():
        status, messageParts = imap.fetch(msgId, '(RFC822)')

        if status != 'OK':
            print('Error fetching mail.')

        emailBody = messageParts[0][1]
        raw_emailBody = emailBody.decode('utf-8')
        mail = email.message_from_string(raw_emailBody)

        for part in mail.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            fileName = part.get_filename()
            print(fileName)

            # Just save XML files
            # must starts with SY3_ are valid .xml files to save
            if (not fileName.startswith('SY3_')):
                continue

            if bool(fileName):
                # filePath = os.path.join(detach_dir, 'xml', fileName)
                filePath = os.path.join('xml', fileName)
                if not os.path.isfile(filePath) :
                    print(fileName)
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
    imap.close()
    imap.logout()

if __name__ == "__main__":
    main()