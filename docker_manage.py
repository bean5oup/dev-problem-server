import docker
import subprocess


client = docker.from_env()

problems = subprocess.check_output(['ls ./problems'], shell=True).decode().split('\n')
problems.remove('')

def build_images():	

	if 'docker-compose.yml' in problems:
		subprocess.run(['docker-compose build'], shell=True, cwd="./problems")
		problems.remove('docker-compose.yml')
	
	for problem in problems:
		check_yml = subprocess.check_output([f'ls ./problems/{problem}'], shell=True).decode().split('\n')
		if 'docker-compose.yml' in check_yml:
			subprocess.run(['docker-compose build'], shell=True, cwd=f'./problems/{problem}')
		else:
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

