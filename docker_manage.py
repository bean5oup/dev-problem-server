import docker
import os

client = docker.from_env()

def build_images():	

	for problem in os.listdir('./problems'):
		client.images.build(path=f'./problems/{problem}', tag=f'{problem}', rm=True)	

	for image in client.images.list():
		if image.tags == []:
			client.images.prune()


def run_container(user_token, problem, port):
	
	client.containers.run(problem, detach=True, name=user_token, ports={'12370/tcp':port}, remove=True)


def stop_container(user_token):
	
	for container in client.containers.list():
		if container.name == user_token:
			container.stop(timeout=100)


def remove_container(user_token):
	
	for container in client.containers.list(all):
		if container.name == user_token:
			container.remove()


#======test=======
#build_images()
#run_container(111, "pwn1", 12370)
#run_container(222, "web1", 12371)

#stop_container('111')
#stop_container('222')


