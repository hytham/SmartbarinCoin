""" This is the main block chain class """
import hashlib



from Data.Block import Block

class Blockchain(object):
    def __init__(self):
        self.blocks = []
        self.transactions = []
        self.blocks.append(self.__generate_genasis())

    def __generate_genasis(self):
        """ Generate the genesis block """
        b = Block(prev_hash="########")
        b.id = 0
        b.hash = "----------------"
        b.proof_no = 0
        return b
    def generate_block(self, last_block_hash, proof_of_work, transaction):
        """ generate a block and add it to the chain"""
        b = Block(id=self.last_block.id + 1,
                  prev_hash=last_block_hash,
                  proof_no=proof_of_work,
                  data=transaction);
        self.transactions = []
        self.blocks.append(b)

        return b
    def add_transaction(self, sender, recepient, amount, memo):
        """ Add new transactions to the chain """
        self.transactions.append({
            sender: sender,
            recepient: recepient,
            amount: amount,
            memo: memo
        })

        return True


    @property
    def last_block(self):
        """ get the last block in the chain """
        return self.blocks[-1]









        

