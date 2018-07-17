# Something in lines of http://stackoverflow.com/questions/348630/how-can-i-download-all-emails-with-attachments-from-gmail
# Make sure you have IMAP enabled in your gmail settings.
# Also allowing access to less secure apps, but this may leave your account vulnerable.
# 
# Right now it won't download same file name twice even if their contents are different.

import email
import getpass, imaplib
import os
# import sys
import datetime
from subprocess import call

detach_dir = '.'
detach_dir = '/Users/charliezhu/app/bw/responsys/IFTTT/Gmail'
# if 'attachments' not in os.listdir(detach_dir):
#     os.mkdir(detach_dir + "/" + 'attachments')
# detach_dir = detach_dir + "/attachments"

# userName = input('Enter your GMail username:')
userName = os.environ.get("RESPONSYS_GMAIL")
# passwd = getpass.getpass('Enter your password: ')
passwd = os.environ.get("RESPONSYS_GMAIL_PASSWD")

try:
    imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
    return_code, accountDetails = imapSession.login(userName, passwd)
    if return_code != 'OK':
        print('Not able to sign in!')
        raise
    
    labels = imapSession.list()[1]
    # imapSession.select('[Gmail]/All Mail')
    for l in labels:
        print(l)
    imapSession.select('INBOX')
    # return_code, data = imapSession.search(None, 'ALL')
    return_code, data = imapSession.search(None, '(UNSEEN)')
    if return_code != 'OK':
        print('Error searching Inbox.')
        raise
    
    # Iterating over all emails
    for msgId in data[0].split():
        return_code, messageParts = imapSession.fetch(msgId, '(RFC822)')
        if return_code != 'OK':
            print('Error fetching mail.')
            raise

        emailBody = messageParts[0][1]
        mail = email.message_from_bytes(emailBody)
        for part in mail.walk():
            if part.get_content_maintype() == 'multipart':
                # print(part.as_string())
                continue
            if part.get('Content-Disposition') is None:
                # print(part.as_string())
                continue
            fileName = part.get_filename()

            if bool(fileName):
                # print("Raw Date: ", mail["Date"])
                # 'Sun, 15 Jul 2018 08:07:08 +0000'
                date_tuple = email.utils.parsedate_tz(mail['Date'])
                local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
                date_suffix = local_date.strftime("%Y-%m-%d")
                fileName = fileName + "." + date_suffix

                filePath = os.path.join(detach_dir, fileName)
                if not os.path.isfile(filePath) :
                    print(fileName)
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
                else:
                    print(fileName + " was already downloaded.")
    imapSession.close()
    imapSession.logout()
    call('pwd')
    call('/Users/charliezhu/work/bin/email_metrics_load.sh')
except (Exception) as error: 
    print(error)
    print('Not able to download all attachments.')

