import docker
import subprocess

client = docker.from_env()

problems = subprocess.check_output(['ls ./problems'], shell=True).decode().split('\n')
problems.remove('')

def build_images():	

	if 'docker-compose.yml' in problems:
		print('build using docker-compose.yml')
		subprocess.run(['docker-compose build'], shell=True, cwd="./problems")
	
	else:	
		for problem in problems:
			client.images.build(path=f'./problems/{problem}', tag=f'{problem}', rm=True)	

	for image in client.images.list():
		if image.tags == []:
			client.images.prune()


def run_container(user_token, problem, port):
	
	client.containers.run(problem, detach=True, name=user_token, ports={'8080/tcp':port}, remove=True)


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
#run_container(333, "web1", 12372)

#stop_container('111')
#stop_container('222')
#stop_container('333')

