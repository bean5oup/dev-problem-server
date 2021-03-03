import time
import docker_manage


check_disconnection = {}

def check_timelimit(usertoken, timelimit):
	
	if timelimit == -1: # No timelimit
		return

	start = time.time()

	while time.time() - start < timelimit:
		time.sleep(1)
		if check_disconnection[usertoken] == True:

			print("[*] Detecting disconnection during checking timelimit for {}".format(usertoken))
			check_disconnection.pop(usertoken)
			return


	docker_manage.stop_container(usertoken)
	check_disconnection.pop(usertoken)
	print('[+] docker stop container : {} : from timelimit'.format(usertoken))

	return
