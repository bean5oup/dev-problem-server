import psutil

strings = ''
stringsFormat = '%-30s\t%-30s\t%-10s\t%-30s\t%-10s\n'
strings = stringsFormat % ('process', 'local ip', 'local port', 'remote ip', 'remote port')
strings += '-'*30+'\t'+'-'*30+'\t'+'-'*10+'\t'+'-'*30+'\t'+'-'*10+'\n'


personalPort = [i for i in range(49152, 65536)]
usedPort = []

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

def main():


        for con in psutil.net_connections():
                if conn.status == 'NONE':
                        pass

        return


if __name__ == '__main__':
        sample()


# https://psutil.readthedocs.io/en/latest/



