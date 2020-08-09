from timeit import default_timer as timer
from unittest import TestCase

from Data import Blockchain


class TestBlockchain(TestCase):
    def test_creat_block_chain(self):
        blockChain = Blockchain.Blockchain()
        assert len(blockChain.blocks) == 1
        assert blockChain.blocks[0].hash == "----------------"

    def test_get_last_block(self):
        blockChain = Blockchain.Blockchain()
        last_block = blockChain.get_last_block()
        assert last_block.hash == "----------------"

    def test_add_a_single_new_block(self):
        blockChain = Blockchain.Blockchain()
        prev_block_hash = blockChain.get_last_block_hash()
        blockChain.generate_block(prev_block_hash,3,[])
        assert len(blockChain.blocks) == 2

    def test__calculate_merkal_root(self):
        bc = Blockchain.Blockchain()
        transactions =['1','2','3','4']
        root = bc._calculate_merkal_root(transactions)
        self.assertIsNotNone(root)
        self.assertEqual("88cd668c2056e926cf9f6dad3acbeebf0c1e093da5ab7aceb244e65661d7e35e",root)

    def test_calculate_hash_rate(self):
        bc = Blockchain.Blockchain()
        start= timer()
        block = bc.calculate_hash_rate


        end = timer()
