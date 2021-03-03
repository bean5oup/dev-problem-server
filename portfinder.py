import psutil

def processinfo(conn):

        process = psutil.Process(conn.pid)

        return process.name()


def findUsablePort():


        usablePort = {}
        for i in range(50000, 65536):
                usablePort[i] = True


        for conn in psutil.net_connections():
                if conn.status == 'NONE':
                        pass
                else:
                        localport = int(conn.laddr[1])
                        usablePort[localport] = False


        print("[*] Using Port : ", end='')
        for i in usablePort:
                if usablePort[i] == True:
                        
                        print(str(i))
                        
                        return i


        return -1

findUsablePort()
# https://psutil.readthedocs.io/en/latest/
# https://blog.itanoss.kr/ko/python%EC%9C%BC%EB%A1%9C-docker-%EC%BB%A8%ED%8A%B8%EB%A1%A4%ED%95%98%EA%B8%B0/



