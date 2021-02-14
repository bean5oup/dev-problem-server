import docker
import os


client = docker.from_env()

os.chdir('/Users/kangwoosun/Desktop/Woosun/github/dev-problem-server')

client.images.build(path='./', tag='test')