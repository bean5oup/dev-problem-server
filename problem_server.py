import socket
import portfinder
import threading
import docker_manage
import portfinder
import time_limit
from enum import Enum


class problem_request(Enum):
	START = 1
	DISCONNECTION = 2


class problem_socket:


	def __init__(self, max=0, host="localhost", port=None):


		if port is None:
			print("[-] None port error : (problem_socket, __init__)")
			return -1

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.receive_request = ''
		self.send_request = ''
		self.host = host
		self.port = port
		self.max = max

		print("[+] sock binding")


		self.sock.bind((host, port))


	def dockerService(self, usertoken, problem_name, request_type, timelimit):

		usable_port = portfinder.findUsablePort()

		if usable_port == -1:
			print('[-] find usable port error : (problem_socket, dockerService)')
			exit()


		if request_type == problem_request.START.value:

			print('[+] docker run container : {}'.format(problem_name))
			docker_manage.run_container(usertoken, problem_name, usable_port)

			time_limit.check_disconnection.update({usertoken : False})
			t = threading.Thread(target=time_limit.check_timelimit, args=(usertoken, timelimit))
			t.daemon = True
			t.start()


		elif request_type == problem_request.DISCONNECTION.value:

			print('[+] docker stop container : {}'.format(problem_name))
			docker_manage.stop_container(usertoken)

			time_limit.check_disconnection[usertoken] = True



		else:
			print('[-] request_type error : (problem_socket, dockerService)')


		return


	def receiveRequest(self, client_socket, addr):

		print("[*] receiveRequest")
		print("[*] client_socket : {}".format(client_socket))
		print("[*] addr : {}".format(addr))
		msg = client_socket.recv(2048).decode('latin-1')
		print("[*] msg : {}".format(msg))
		

		usertoken = msg.split(':')[0]
		problem_name = msg.split(':')[1]
		request_type = msg.split(':')[2]
		
		try: 
			timelimit = msg.split(':')[3]

		except IndexError:
			timelimit = -1 # No time limit


		print("[*] usertoken : {}".format(usertoken))
		print("[*] problem_name : {}".format(problem_name))
		print("[*] request_type : {}".format(request_type))
		print("[*] time_limit : {}".format(timelimit))

		self.dockerService(usertoken, problem_name, int(request_type), int(timelimit))


		client_socket.close()

		return

	def waiting(self):

		docker_manage.build_images()

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

			t = threading.Thread(target=problem_socket.receiveRequest, args=(self, client_socket, addr))
			t.daemon = True
			t.start()

		return 0


	def connect(self, host, port):
	    self.sock.connect((host, port))


	def mysend(self, msg):
	    totalsent = 0
	    sent = self.sock.send(msg)
	    if sent == 0:
	        raise RuntimeError("socket connection broken")
	    

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



	def __del__(self):
		if self.sock != None:
			self.sock.close()

		return
