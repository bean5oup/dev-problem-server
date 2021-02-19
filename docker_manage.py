import docker
import os

client = docker.from_env()

#client.images.build(paht='./', tag='test')
#os.chdir('/Users/kangwoosun/Desktop/Woosun/github/dev-problem-server')
#print(client.images.get('test'))

def build_images():
	for i in os.listdir('./problems'):
		client.images.build(path=f'./problems/{i}', tag=f'{i}', rm=True)	

def run_container(user_token, problem, port):
	client.containers.run(problem, detach=True, name=user_token, ports={'12370/tcp':port})

def stop_container(user_token):
	for container in client.containers.list():
		if container.name == user_token:
			container.stop()

def remove_container(user_token):
	for container in client.containers.list(all):
		if container.name == user_token:
			container.remove()

#======test=======
#build_images()
#run_container(111, "pwn1", 12370)
#run_container(222, "pwn1", 12371)

#stop_container('111')
#stop_container('222')

#remove_container('111')
#remove_container('222')



