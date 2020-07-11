import socket
import threading
import time
import traceback

from requests import get


def debug( msg ):
    print("[%s] %s" % (str(threading.currentThread().getName()), msg))

class P2PNode:
    def __init__(self,serverport,id=None,serverhost = None,debug=True):
        self.serverport = serverport
        self.debug = debug
        self.serverhost = serverhost
        self.peers = {}
        self.router = None
        self.shotdown = False
        self.id = id
        self.is_setup = True
        self.MAX_BUFFER_SIZE=10000

    def setup(self):
        if self.serverhost == None:
            self.serverhost = self._get_host_from_remote()
        if id:
            self.id = id
        else:
            self.id = '%s:%d' % (self.serverhost, self.serverport)

        self.is_setup = True
    def _get_host_from_remote(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(("www.google.com",80))
        self.hostname = s.getsockname()[0]
        s.close()
        return self.hostname
    def _get_public_ip_address(self):
        ip = get('https://api.ipify.org').text
        return ip
    def _handlepeer(self,clientsock):
        debug('New child ' + str(threading.currentThread().getName()))
        debug('Connected ' + str(clientsock.getpeername()))
        host, port = clientsock.getpeername()
        recived_data = self.receivedata(clientsock)

        """ Add code to handle the message and sendback a reply """

        clientsock.close()
        clientsock = None
    def receivedata(self, clientsock):
        total_data = []
        try:
            data = clientsock.recv(self.MAX_BUFFER_SIZE)
            if data:
                total_data.append(data)
            else:
                time.sleep(0.1)
        except:
            pass

        return data
    def _makeserversocket(self,port,backlog=5):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', port))
        s.listen(backlog)
        return s
    def send(self,socket,message):
        socket.send(message.encode('utf8'))
    def sendtopeer(self,peerid,message):
        if self.router:
            nextpid,host,port = self.router(peerid)
        return self.connectandsend(nextpid,host,port,message)
    def connectandsend(self,peerid,host,port,message):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, int(port)))
        s.send(message.encode('utf8'))

    def addhandler(self,msgtype,handler):
        self.handler[msgtype] = handler

    def addrouter(self,router):
        self.router=router

    def addpeer(self,peerid,host,port):
        if peerid not in self.peers and (self.maxpeers == 0 or
                                         len(self.peers) < self.maxpeers):
            self.peers[peerid] = (host, int(port))
            return True
        else:
            return False

    def getpeer(self,peerid):
        assert peerid in self.peers
        return self.peers[peerid]
    def delpeer(self,peerid):
        if peerid in self.peers:
            del self.peers[peerid]
    def numberofpeers(self):
        return len(self.peers)

    def mainloop(self):
        if self.is_setup == False :
            raise Exception("You must call setup first befor running the main loop")

        s = self._makeserversocket(self.serverport)
        debug( 'Server started: %s (%s:%d)'
		      % ( self.id, self.serverhost, self.serverport ) )

        while not self.shotdown:
            try:

                clientsocket , clientaddress = s.accept()
                t = threading.Thread(target = self._handlepeer, args = [clientsocket])
                t.start()

            except:
                if self.debug:
                    traceback.print_exc()
                    continue








