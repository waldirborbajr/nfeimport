import imaplib
import email.header
import os
import sys

# Your IMAP Settings
host = 'imap.host.com'
user = 'email@adrs.com'
password = 'passwd'

# Connect to the server
print('Connecting to ' + host)
mailBox = imaplib.IMAP4_SSL(host)

# Login to our account
mailBox.login(user, password)

boxList = mailBox.list()
# print(boxList)

mailBox.select()
searchQuery = '(SUBJECT "Desired Subject")'

result, data = mailBox.uid('search', None, searchQuery)
ids = data[0]
# list of uids
id_list = ids.split()

i = len(id_list)
for x in range(i):
    latest_email_uid = id_list[x]

    # fetch the email body (RFC822) for the given ID
    result, email_data = mailBox.uid('fetch', latest_email_uid, '(RFC822)')
    # I think I am fetching a bit too much here...

    raw_email = email_data[0][1]

    # converts byte literal to string removing b''
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)

    # downloading attachments
    for part in email_message.walk():
        # this part comes from the snipped I don't understand yet...
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()

        if bool(fileName):
            filePath = os.path.join('C:/DownloadPath/', fileName)
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()

    subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
    print('Downloaded "{file}" from email titled "{subject}" with UID {uid}.'.format(file=fileName, subject=subject, uid=latest_email_uid.decode('utf-8')))

mailBox.close()
mailBox.logout()