import threading
import time
from unittest import TestCase

from Net.NodeConnection import NodeConnection


class TestNodeConnection(TestCase):
    def test_makeserversocket(self):
        connection = NodeConnection(port=300)
        connection.makeserversocket()
        self.assertTrue(True)

    def test_connectandsend(self):
        t = threading.Thread(target=self._mainloop)
        t.start()

        time.sleep(10)
        connection = NodeConnection(port=3001)
        connection.connectandsend("127.0.0.1",3000,"test")


    def _mainloop(self):
        connection = NodeConnection(port=3000)
        connection.makeserversocket()
        clientsocket,clientaddress = connection.accept()
        data = connection.receivedata(clientsocket)

        self.assertEqual(b'test',data)


