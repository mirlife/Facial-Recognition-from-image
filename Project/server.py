import socket
import threading
import hashlib
import time

from jpegg import *

serversock = socket.socket()
host = socket.gethostname();
port = 9000;
serversock.bind((host,port));
filename = ""
serversock.listen(100000);
print ("Waiting for a connection.....")
imagePath = 'test/'


def writes(clientsocket):
	while True:
	    size = clientsocket.recv(16) 
	    if not size:
	        break
	    size = int(size, 2)
	    filename = clientsocket.recv(size)
	    filesize = clientsocket.recv(32)
	    filesize = int(filesize, 2)
	    file_to_write = open('test/{}'.format(filename.decode(encoding="ascii"))	 , 'wb')
	    chunksize = 4096
	    while filesize > 0:
	        if filesize < chunksize:
	            chunksize = filesize
	        data = clientsocket.recv(chunksize)
	        file_to_write.write(data)
	        filesize -= len(data)

	    file_to_write.close()
	    print ('File received successfully')



while True:
	clientsocket,addr = serversock.accept()
	print("Got a connection from %s" % str(addr))
	client_serve_thread = threading.Thread(target=writes, args=tuple((clientsocket,)))
	client_serve_thread.start()

	with open("scanned.json",'r+',encoding = 'utf-8') as scanned_file:
		scanned = json.loads(scanned_file.read())
		print(f"scanned:  {scanned}")
		files = os.listdir(imagePath)
		print(f"Files : {files}")
		for test_image in files:
			if test_image == 'Thumbs.db':
				files.remove(test_image)
			elif test_image not in scanned:
				print(f"Found new image  {test_image}")
				print("###################PRedicted person:  ",tested(test_image,known_face_encodings,known_face_names),'##############')

				scanned.append(test_image)
				print(f'Going To add ... {scanned}')
				# scanned = []
				scanned_files =  open("scanned.json",'w',encoding = 'utf-8')
				json.dump(scanned,scanned_files)
				print("###### ADDED")
				scanned_files.close()
		time.sleep(5)
	time.sleep(0.001)