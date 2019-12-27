import socket
import os
# import thread

s = socket.socket()
host = socket.gethostname()
port = 9000
s.connect((host, port))
print("Connected to server ..")
path = 'screenshots_to_send'
directory = os.listdir(path)
print(f"############    Len of dir {len(directory)}")
for files in directory:
    print (files)
    filename = files
    size = len(filename)
    size = bin(size)[2:].zfill(16) # encode filename size as 16 bit binary
    s.send(bytes(size,'utf-8'))
    s.send(bytes(filename,'utf-8'))

    filename = os.path.join(path,filename)
    filesize = os.path.getsize(filename)
    filesize = bin(filesize)[2:].zfill(32) # encode filesize as 32 bit binary
    s.send(bytes(filesize,'utf-8'))
    

    file_to_send = open(filename, 'rb')

    l = file_to_send.read()
    s.sendall(l)
    file_to_send.close()
    print ('File Sent')

s.close()