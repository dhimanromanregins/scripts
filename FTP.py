from ftplib import FTP_TLS
import os

# FTP credentials
host = 'waws-prod-dm1-301.ftp.azurewebsites.windows.net'
username = '$stgkpbariatricsapi'
password = 'AQKFZZzBUGE_QJ-kkqUW1mtVA9w7sgE.noQhvMwXdG2q8qUqzZXM4ZMkQcZffwNauaYDYiT5Vvo'

# Local and remote directories
local_dir = '/var/lib/jenkins/workspace/Backend_CICD/Member.Qst.Services/Member.Qst.Api/bin/Debug/net6.0/publish/'
remote_dir = '/site/wwwroot'

# Connect to FTP server
ftp = FTP_TLS(host)
ftp.login(username, password)

# Change to the remote directory
ftp.cwd(remote_dir)

# Upload files recursively
def upload_files(local_dir):
    for item in os.listdir(local_dir):
        if os.path.isfile(os.path.join(local_dir, item)):
            with open(os.path.join(local_dir, item), 'rb') as f:
                ftp.storbinary('STOR ' + item, f)
        elif os.path.isdir(os.path.join(local_dir, item)):
            ftp.mkd(item)
            ftp.cwd(item)
            upload_files(os.path.join(local_dir, item))
            ftp.cwd('..')

upload_files(local_dir)

# Quit FTP connection
ftp.quit()
