"""
The building block of any block chain is the block object that have the following attributes
id: the Id of the block
hash: the block hash
prev_hash: the previous block hash
next_hash: the next block hash
nonce: the block nonce during mining
permission: dictionary to tell which role have which permissions
data: the payload that will be saved in this blok, it can be a transaction or a binary (TBD)
"""
import json
import time

from Data.Cryptotools import generate_hash

""" Is the main building block of a block chain """
class Blockbody:
    def __init__(self,data):
        self.data = data

    def __repr__(self):
        return self.data

class Blockheader:
    def __init__(self,id=0,prev_hash=None,block_hash = None, proof_no=None,timestamp=None):
        self.id = id
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.proof_no = proof_no
        self.merkel_root = ""

    def __repr__(self):
        return "id = {} , hash = {} , prev_hash = {} , next_hash = {} , proof_no = {}" \
            .format(self.id, self.hash, self.prev_hash, self.next_hash, self.proof_no)

class Block(object):
    def __init__(self, id=0,prev_hash=None, proof_no=None, permission=None, data=None):
       ts = self.__get_time_stamp()

       self.header = Blockheader(id,prev_hash,proof_no,timestamp=ts)
       self.body = Blockbody(data)

       self.header.hash = self.get_hash()

    def to_json(self):
        """ return a json string of this block """
        return json.dumps(self)

    def from_json(self, block_json):
        """ load a json string to this block """
        self = json.loads(block_json)

    def __get_time_stamp(self):
        """ Generate a timestamp """
        return int(round(time.time() * 1000))

    def get_hash(self):
        """ generate a hash for this block using the timestamp the previous hash and the data """
        str = "{}{}{}{}".format(self.header.timestamp, self.header.prev_hash, self.body.data,self.header.proof_no)
        return generate_hash(str)