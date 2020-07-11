from unittest import TestCase

from Blockchain.Block import Block


class TestBlock(TestCase):
    def test_create_genasis_block(self):
        block = Block.generate_genasis()
        assert block.prev_hash == "########"
        assert block.hash == "----------------"
        
    def test_create_block(self):
        gen_block = block = Block.generate_genasis()
        block = Block.generate_block(last_block=gen_block,nonce=100,transaction={})
        assert block.prev_hash == "----------------"
        assert block.nonce == 100

        

    def test_update_next_hash(self):
        gen_block = block = Block.generate_genasis()
        block = Block.generate_block(last_block=gen_block, nonce=100, transaction={})
        block2 = Block.generate_block(last_block=gen_block, nonce=100, transaction={})
        block.update_next_hash(block2.hash)

        assert block.next_hash == block2.hash



    def test_to_string(self):
        gen_block = Block.generate_genasis().to_string()

        assert gen_block == "id = 0 , hash = ---------------- , prev_hash = ######## , next_hash = None , nonce = None , permission = None , data = None"
        print(gen_block)

    def test_to_json(self):
        gen_block = Block.generate_genasis().to_json()
        print(gen_block)

    def test_from_json(self):
        self.fail()
