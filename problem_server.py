import socket
import portfinder
import threading


class problem_socket:

    def __init__(self, max=0, file='', host="localhost", port=None):
        

        if port is None:
        	print("[-] None port error : (problem_socket, __init__)")
        	return -1

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.receive_request = ''
        self.send_request = ''
        self.host = host
        self.port = port
        self.max = max
        self.file = file

        print("[+] sock binding")


        self.sock.bind((host, port))

    def waiting(self):

    	if self.sock == None:
    		print("[-] None sock error : (problem_socket, waiting)")
    		return -1

    	self.sock.listen(self.max)

    	while True:
    		try:
    			print("[*] Waiting for client")
    			client_socket, addr = self.sock.accept()

    		except KeyboardInterrupt:
    			self.sock.close()
    			print("[*] KeyboardInterrupt")
    			break

    		print("[+] Receive request")

    		t = threading.Thread(target=receiveRequest, args=(client_socket,addr))
    		t.daemon = True
    		t.start()

    	return 0


    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent


    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)


    def receiveRequest(client_socket, addr):

    	print("[*] receiveRequest")
    	print("[*] client_socket : {}".format(client_socket))
    	print("[*] addr : {}".format(addr))



    	return