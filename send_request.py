from problem_server import *



s = problem_socket(port = 8082)
s.connect('localhost', 8080)

s.mysend(b'admin:pwn1:1:123') # pwn1 images run container
#s.mysend(b'admin:pwn1:2') # pwn1 images stop container


# request
# usertoken:problem's id or name:request_type:timelimit

