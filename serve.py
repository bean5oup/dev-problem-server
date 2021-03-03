import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--port", help="Port for problem_server to listen on", default=8080)
parser.add_argument("--max", help="Set the maximum number of dockers to run", default=20)

args = parser.parse_args()


print("[*] port : {}".format(args.port))
print("[*] max : {}".format(args.max))

from problem_server import *

server_socket = problem_socket(port=int(args.port), max=int(args.max))
server_socket.waiting()
