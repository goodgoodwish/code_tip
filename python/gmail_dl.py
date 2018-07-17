"""

This module demonstrates Something in lines of http://stackoverflow.com/questions/348630/how-can-i-download-all-emails-with-attachments-from-gmail
Make sure you have IMAP enabled in your gmail settings.
Also allowing access to less secure apps, but this may leave your account vulnerable.

It will skip the file if same file name is in local disk.

Example:
    $> python gmail_dl.py

Attributes:

Todo:
    * Rewrite with google-api-python-client oauth2client.


"""

import email
# import getpass
import imaplib
import os
import datetime
from subprocess import call

def get_attachement(detach_dir:str):
    """Download gmail attachment using IMAP
    
    Only search INBOX label, for new unread emails.
    Append email date to file name.

    Args:
        parma1(str): .....

    Returns:
        value1(data type): ....

    """
    # if 'attachments' not in os.listdir(detach_dir):
    #     os.mkdir(detach_dir + "/" + 'attachments')
    # detach_dir = detach_dir + "/attachments"

    # user_name = input('Enter your GMail user_name:')
    user_name = os.environ.get("RESPONSYS_GMAIL")
    # passwd = getpass.getpass('Enter your password: ')
    passwd = os.environ.get("RESPONSYS_GMAIL_PASSWD")

    try:
        imap_session = imaplib.IMAP4_SSL('imap.gmail.com')
        return_code, account_details = imap_session.login(user_name, passwd)
        if return_code != 'OK':
            print('Not able to sign in!')
            raise
        
        labels = imap_session.list()[1]
        # imap_session.select('[Gmail]/All Mail')
        for l in labels:
            print(l)
        imap_session.select('INBOX')
        # return_code, data = imap_session.search(None, 'ALL')
        return_code, data = imap_session.search(None, '(UNSEEN)')
        if return_code != 'OK':
            print('Error searching Inbox.')
            raise
        
        # Iterating over all emails
        for msgId in data[0].split():
            return_code, message_parts = imap_session.fetch(msgId, '(RFC822)')
            if return_code != 'OK':
                print('Error fetching mail.')
                raise

            email_body = message_parts[0][1]
            mail = email.message_from_bytes(email_body)
            for part in mail.walk():
                if part.get_content_maintype() == 'multipart':
                    # print(part.as_string())
                    continue
                if part.get('Content-Disposition') is None:
                    # print(part.as_string())
                    continue
                file_name = part.get_file_name()

                if bool(file_name):
                    # print("Raw Date: ", mail["Date"])
                    # 'Sun, 15 Jul 2018 08:07:08 +0000'
                    date_tuple = email.utils.parsedate_tz(mail['Date'])
                    local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
                    date_suffix = local_date.strftime("%Y-%m-%d")
                    file_name = file_name + "." + date_suffix

                    file_path = os.path.join(detach_dir, file_name)
                    if not os.path.isfile(file_path):
                        print(file_name)
                        fp = open(file_path, 'wb')
                        fp.write(part.get_payload(decode=True))
                        fp.close()
                    else:
                        print(file_name + " was already downloaded.")
        imap_session.close()
        imap_session.logout()
        call('pwd')
        call('/Users/charliezhu/work/bin/email_metrics_load.sh')
    except (Exception) as error:
        print(error)
        print('Not able to download all attachments.')

if __name__ == '__main__':
  get_attachement(detach_dir = '/Users/charliezhu/app/bw/responsys/IFTTT/Gmail')

