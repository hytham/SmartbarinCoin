from unittest import TestCase

from Net.Protocol import Payload


class TestProtocol(TestCase):
    def test_invoke(self):
        self.fail()

    def test_generate_response(self):
        self.fail()


class TestPayload(TestCase):
    def test_parse(self):
        message = 'TEST|4|1595046069.3078604|532eaabd9574880dbf76b9b8cc00832c20a6ec113d682299550d7a6e0f345e25|Test'
        payload = Payload(seperator='|')
        payload.parse(message)
        self.assertEqual("TEST",payload.header.command)

    def test_parse_diffrant_hash(self):
        message = 'TEST|4|1595046069.3078604|532eaabd9574880db6b9b8cc00832c20a6ec113d682299550d7a6e0f345e25|Test'
        payload = Payload(seperator='|')
        payload.parse(message)
        self.assertEqual("TEST", payload.header.command)





    def test_create(self):
        payload = Payload(seperator='|')
        payload.create("TEST","Test")

        str = payload.get_payload()
        print(str)
        self.assertTrue(True)

    def test_get_protocol_action(self):
        payload = Payload(seperator='|',protocol_action=[()])
        x = _get_protocol_action("TEST")


