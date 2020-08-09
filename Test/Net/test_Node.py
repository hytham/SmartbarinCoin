import time
from unittest import TestCase

from Net.Node import Node
from Net.Protocol import Protocol


class TestBlockChainProtocol(TestCase):


    def test_send_loop_back(self):
        protocol = Protocol()
        p2p = Node(protocol,port=3000)
        p2p_sender = Node(protocol,port=3001)



        p2p.run()
        p2p_sender.run()

        time.sleep(3)

        p2p_sender.connectandsend(host="127.0.0.1",port=3000,message="test")

        time.sleep(3)
        msg1 = p2p.get_recived_message()

        time.sleep(10)

        msg2 =p2p_sender.get_recived_message()

        p2p.shutdown()
        p2p_sender.shutdown()

        self.assertEqual("test",msg1)
        self.assertEqual("<PING>test</PING>", msg2)


