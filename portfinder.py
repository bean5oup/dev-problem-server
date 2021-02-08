import psutil

strings = ''
stringsFormat = '%-30s\t%-30s\t%-10s\t%-30s\t%-10s\n'
strings = stringsFormat % ('process', 'local ip', 'local port', 'remote ip', 'remote port')
strings += '-'*30+'\t'+'-'*30+'\t'+'-'*10+'\t'+'-'*30+'\t'+'-'*10+'\n'


localip = ''
localport = ''
remoteip = ''
remoteport = ''

def processinfo(conn):
        process = psutil.Process(conn.pid)
        return process.name()

def sample():

        global strings

        for conn in psutil.net_connections():
                        
                if conn.status == 'NONE':
                        pass

                else:
                                
                        localip = conn.laddr[0]
                        localport = conn.laddr[1]
                        remoteip = conn.raddr[0] if conn.raddr else '-'
                        remoteport = conn.raddr[1] if conn.raddr else '-'
                        

                        strings += stringsFormat % (processinfo(conn), localip, localport, remoteip, remoteport)


        print(strings)

        return

def findUsablePort():


        usablePort = {}
        for i in range(50000, 65536):
                usablePort[i] = True


        for conn in psutil.net_connections():
                if conn.status == 'NONE':
                        pass
                else:
                        localport = int(conn.laddr[1])
                        personalPort[localport] = False


        print("[*] Using Port : ", end='')
        for i in personalPort:
                if personalPort[i] == True:
                        
                        print(str(i))
                        
                        return i


        return -1

def main():




if __name__ == '__main__':
        main()


# https://psutil.readthedocs.io/en/latest/
# https://blog.itanoss.kr/ko/python%EC%9C%BC%EB%A1%9C-docker-%EC%BB%A8%ED%8A%B8%EB%A1%A4%ED%95%98%EA%B8%B0/



