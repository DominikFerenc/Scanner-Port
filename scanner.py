from socket import *


class LocalScanner:
    def getHostToscanned(self):
        host = input("Enter to host to scanned: ")
        return gethostbyname(host)

    def getLowestPort(self):
        return int(input("Enter to lowest port: "))

    def getMaximumPort(self):
        return int(input("Enter to maximum port: "))

    def startingScan(self, ip_to_host, lowest_port, maximum_port):
        print("\nStarting scan on host:\033[33m",
              ip_to_host, "\033[0min the range of:\033[32m", lowest_port, "\033[0mport to:\033[31m", maximum_port, "\033[0mport")

    def showOpenPorts(self, port):
        print('Port \033[33m%d\033[0m: \033[32m Open\033[0m' % port)

    def setSocket(self):
        ip_to_host = self.getHostToscanned()
        lowest_port = self.getLowestPort()
        maximum_port = self.getMaximumPort()
        self.startingScan(ip_to_host, lowest_port, maximum_port)

        for port in range(lowest_port, maximum_port):
            newSocket = socket(AF_INET, SOCK_STREAM)
            connection = newSocket.connect_ex(((ip_to_host, port)))
            if (connection == 0):
                self.showOpenPorts(port)
            newSocket.close()



#class Data:
    #def getAvailablePorts(self):
    #def presentationData(self):




def main():
    sc = LocalScanner()
    try:
        sc.setSocket()
    except (KeyboardInterrupt, SystemExit):
        print("\n\033[31mThe key combination CTRL+C is pressed.\033[0m")

if __name__ == "__main__":
    main()
