import time
from unittest import TestCase

from Net.Node import Node
from Net.NodeConnection import NodeConnection
from Net.Protocol import Protocol, Payload


class TestBlockChainProtocol(TestCase):
    def test_generate_response(self):
        p2p = Protocol()
        resp = p2p.GenerateResponse("test")
        self.assertEqual("<PING>test</PING>",resp)

    def test_send_loop_back(self):
        payload = Payload()

        payload.create("TEST",'')

        (msg1,msg2) = self._handshake_server_client(3000,3001,str(payload),{})

        self.assertEqual("test",msg1)
        self.assertEqual("<PING>test</PING>", msg2)

    def test_send_node_is_alive(self):

        (msg1,msg2) = self._handshake_server_client(3000,3001,"PING",{})

        self.assertEqual("test", msg1)
        self.assertEqual("<PING>I am a live</PING>", msg2)


    def _handshake_server_client(self,server_port1,server_port2,sending_message,content):


        p2p = Node(port=server_port1)
        p2p_sender = Node(port=server_port2)

        p2p.run()
        p2p_sender.run()

        time.sleep(5)

        p2p_sender.connectandsend(host="127.0.0.1", port=server_port1, message=sending_message)

        time.sleep(5)
        msg1 = p2p.get_recived_message()

        time.sleep(5)

        msg2 = p2p_sender.get_recived_message()

        p2p.shutdown()
        p2p_sender.shutdown()

        return (msg1,msg2)

