from problem_server import *



s = problem_socket(port = 8082)
s.connect('localhost', 8080)
s.mysend(b'admin:pwn:1')

# request
# usertoken:problem's id or name:request_type
