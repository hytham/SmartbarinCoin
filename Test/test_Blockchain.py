from unittest import TestCase

from Block import Block
from Blockchain import Blockchain


class TestBlockchain(TestCase):
    def test_creat_block_chain(self):
        blockChain = Blockchain()
        assert blockChain.get_length() == 1
        assert blockChain.blocks[0].hash == "----------------"

    def test_get_last_block(self):
        blockChain = Blockchain()
        last_block = blockChain.get_last_block()
        assert last_block.hash == "----------------"

    def test_add_a_single_new_block(self):
        blockChain = Blockchain()
        blockChain.add_block({})

        assert blockChain.get_length() == 2





