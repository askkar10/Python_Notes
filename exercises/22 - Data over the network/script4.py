import paramiko
t = paramiko.Transport(hostname,port)
t.connect(username,password)
sftp = paramiko.SFTPClient.from_transport(t)