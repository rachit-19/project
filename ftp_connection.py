import ftplib

ftp = ftplib.FTP()
host = "ftp.webmaze.in"
port = 21
ftp.connect(host, port)

