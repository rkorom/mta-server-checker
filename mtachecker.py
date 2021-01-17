import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import psutil

# MTA
path = "/srv/mtapub"
procname = "mta-server64"

# EMAIL
smtp_host = 'host'
smtp_user = "username"
smtp_pass = "password"
email_from = 'from'
email_to = 'to'


def checkprocessrun(name):
    for proc in psutil.process_iter():
        try:
            if name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

if __name__ == "__main__":
    if not checkprocessrun(procname):
        print("SERVER NOT RUNNING")
        
        # restart
        os.system("killall -9 mta-server64")  # safety kill
        os.system(path + "/mta-server64 -d")  # start

        # email
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = email_to
        msg['Subject'] = 'MTA SERVER RESTARTED'
        body = 'MTA SERVER RESTART BY AUTOMATIC'
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP_SSL(smtp_host, 465)
        server.login(smtp_user, smtp_pass)
        server.sendmail(email_from, email_to, msg.as_string())
        server.quit()

        print("SERVER RESTARTED")
