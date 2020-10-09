from socket import *

class LocalScanner:
    def getHostToscanned(self):
        host = input("Enter to host to scanned:")
        IP_HOST = gethostbyname(host)
        print("Starting scan on host: ", IP_HOST)
        return IP_HOST
    def setSocket(self):
        ip_to_host = self.getHostToscanned()
        for i in range(50, 500):
            newSocket = socket(AF_INET, SOCK_STREAM)
            connection = newSocket.connect_ex(((ip_to_host, i)))
            if (connection == 0):
                print('Port %d: Open' % i)
        newSocket.close()



def main():
    sc = LocalScanner()
    sc.setSocket()

if __name__ == "__main__":
    main()
