import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--port", help="Port for problem_server to listen on", default=8080)
parser.add_argument("--max", help="Set the maximum number of dockers to run", default=20)
parser.add_argument("--file", help="Name of problem's docker file", action="store_true")

args = parser.prase_args()


if args.file:

	


else:
	
	print("[-] please setting location of docker file")
	exit(-1)