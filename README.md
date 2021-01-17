# GTA:SA MTA server checker
Automatic server checker for GTA San Andreas Multi Theft Auto.
When the server down, the software is auto restart it and send email for you.

## Installation and Setup

### 1. Required libs
```python
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import psutil
```

### 2. Change MTA config
Change ```path``` to your server root directory.

Example:
```python
path = "/srv/mtapub"
```

Change ```procname``` according to your server's architecture.
```python
procname = "mta-server64" # 64 bit server
procname = "mta-server" # 32 bit server
```

### 3. Change email config
Email sender will use SMTP.
```python
# EMAIL
smtp_host = 'host'
smtp_user = "username"
smtp_pass = "password"
email_from = 'from'
email_to = 'to'
```

### 4. Add cron job
Auto check must have a cron job.

Linux example:
1. Edit your crons with terminal: 
```
crontab -e
```
2. Add new cron:
```
* * * * * python3.9 /example/path/mtachecker.py
```