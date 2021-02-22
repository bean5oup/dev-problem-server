from problem_server import *



s = problem_socket(port = 8081)
s.connect('localhost', 8080)
s.mysend('1234')