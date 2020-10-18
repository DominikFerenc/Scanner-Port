from socket import *
import platform
import subprocess


class LocalScanner:
    def getHostToscanned(self):
        host = input("Enter to host to scanned: ")
        return gethostbyname(host)

    def getSystemName(self):
        return platform.system()

    def checkHostAvailability(self, ip_to_host):
        system_name = self.getSystemName()
        if system_name == 'Windows':
            return subprocess.run(["ping", "-n", "1", ip_to_host], stdout=subprocess.PIPE).returncode

        else:
            return subprocess.run(["ping", "-c", "1", ip_to_host], stdout=subprocess.PIPE).returncode

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
        response = self.checkHostAvailability(ip_to_host)
        if response == 0:
            lowest_port = self.getLowestPort()
            maximum_port = self.getMaximumPort()
            self.startingScan(ip_to_host, lowest_port, maximum_port)
            try:
                for port in range(lowest_port, maximum_port):

                    newSocket = socket(AF_INET, SOCK_STREAM)
                    connection = newSocket.connect_ex(((ip_to_host, port)))
                    newSocket.settimeout(5)
                    if connection == 0:
                        self.showOpenPorts(port)
                    # else:
                    # print("Port %d isn't open" % port)
                    if port == maximum_port - 1:
                        print("\033[32mDONE!\033[0m\n")
                    newSocket.close()
            except (KeyboardInterrupt, SystemExit):
                print("\n\033[31mThe key combination CTRL+C is pressed.\033[0m")
        else:
            print("No connection to the host.")



#class Data:
    #def getAvailablePorts(self):
    #def presentationData(self):




def main():
    sc = LocalScanner()
    sc.setSocket()
if __name__ == "__main__":
    main()
