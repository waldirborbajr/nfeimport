# Something in lines of http://stackoverflow.com/questions/348630/how-can-i-download-all-emails-with-attachments-from-gmail
# Make sure you have IMAP enabled in your gmail settings.
# Right now it won't download same file name twice even if their contents are different.

import email
import getpass, imaplib
import os
import sys

import dnlconfig as cfg

detach_dir = '.'
if 'nfe' not in os.listdir(detach_dir):
    os.mkdir('nfe')

userName = cfg.server["EMAIL"]
passwd = cfg.server["PWD"]

def main():
    try:
        imapSession = imaplib.IMAP4_SSL(cfg.server["IMAP"])
        typ, accountDetails = imapSession.login(userName, passwd)
        if typ != 'OK':
            print('Not able to sign in!')
            # raise

        imapSession.select(readonly=False) # so we can mark mails as read
        typ, data = imapSession.search(None, 'ALL')
        if typ != 'OK':
            print('Error searching Inbox.')
            # raise

        # Iterating over all emails
        for msgId in data[0].split():
            typ, messageParts = imapSession.fetch(msgId, '(RFC822)')
            if typ != 'OK':
                print('Error fetching mail.')
                # raise

            emailBody = messageParts[0][1]
            raw_emailBody = emailBody.decode('utf-8')
            mail = email.message_from_string(raw_emailBody)
            for part in mail.walk():
                if part.get_content_maintype() == 'multipart':
                    # print part.as_string()
                    continue
                if part.get('Content-Disposition') is None:
                    # print part.as_string()
                    continue
                fileName = part.get_filename()

                # Just save XML files
                # must starts with SY3_ are valid .xml files to save
                if (not fileName.startswith('SY3_')):
                    continue

                if bool(fileName):
                    filePath = os.path.join(detach_dir, 'xml', fileName)
                    if not os.path.isfile(filePath) :
                        print(fileName)
                        fp = open(filePath, 'wb')
                        fp.write(part.get_payload(decode=True))
                        fp.close()
        imapSession.close()
        imapSession.logout()
    except :
        print('Not able to download all attachments.') 


if __name__ == "__main__":
    main()        