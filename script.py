from ftplib import FTP_TLS

def test_ftp_connection(host, username, password):
    try:
        # Connect to FTP server
        ftp = FTP_TLS(host)
        ftp.login(username, password)

        # If login succeeds, connection is successful
        print("FTP connection successful!")

        # Quit FTP connection
        ftp.quit()
        return True
    except Exception as e:
        # If any exception occurs, print error message
        print(f"FTP connection failed: {e}")
        return False

# FTP credentials
host = 'waws-prod-dm1-301.ftp.azurewebsites.windows.net'
username = '$stgkpbariatricsapi'
password = 'AQKFZZzBUGE_QJ-kkqUW1mtVA9w7sgE.noQhvMwXdG2q8qUqzZXM4ZMkQcZffwNauaYDYiT5Vvo'

# Test FTP connection
test_ftp_connection(host, username, password)
