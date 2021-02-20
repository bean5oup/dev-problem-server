import socket
import portfinder
import threading


class server:

    def __init__(self, sock=None, host="127.0.0.1", port=None, max, file):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

        self.sock.stsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


        if port is None:
        	print("[-] None port error : (server, __init__)")
        	return -1

        self.sock.bind((host, port))

    def waiting(self):

    	while True:
    		try:

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



    	return