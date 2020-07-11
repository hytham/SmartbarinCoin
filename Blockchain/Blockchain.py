""" This is the main block chain class """
import hashlib

from Blockchain.Block import Block


class Blockchain(object):
    def __init__(self):
        """ construct a block chain and add the genesis block """
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
    def block_mining(self,miner_details):
        """ min the blockchain and reword  """
        self.add_transaction(sender=0,recepient=miner_details,amount=1,memo="")
        last_block = self.last_block

        last_proof_no = last_block.proof_no
        proof_no = Blockchain.do_proof_of_work(last_proof_no)
        last_hash = last_block.hash

        block = self.generate_block(proof_of_work=proof_no,last_block_hash=last_hash,transaction=self.transactions)

        return vars(block)

    @property
    def last_block(self):
        """ get the last block in the chain """
        return self.blocks[-1]

    @staticmethod
    def check_validity(self, block, previous_block):
        """ Check validity of two blocks """
        if previous_block.id + 1 != block.id:
            return False
        elif previous_block.hash != block.hash:
            return False
        elif not Blockchain.Verifying_proof(block.proof_no, previous_block.proof_no):
            return False
        elif block.timestamp <= previous_block.timestamp:
            return False
        return True

    @staticmethod
    def do_proof_of_work(last_proof):
        """ Construct a proof of work"""
        proof_no = 0
        while Blockchain.Verifying_proof(proof_no, last_proof) is False:
            proof_no += 1

        return proof_no

    @staticmethod
    def Verifying_proof(last_proof, proof_no):
        """ Verify the last proof of work """
        guss = f'{last_proof}{proof_no}'.encode()
        guss_hash = hashlib.sha256(guss).hexdigest()
        return guss_hash[:4] == "0000"





        

