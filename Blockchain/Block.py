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
import hashlib as henc

""" Is the main building block of a block chain """


class Block(object):
    def __init__(self, id=0,prev_hash=None, proof_no=None, permission=None, data=None):
        self.id = id
        self.timestamp = self.__get_time_stamp()
        self.prev_hash = prev_hash
        self.proof_no = proof_no
        self.data = data
        self.hash = self.__get_hash()



    def to_string(self):
        """ returns  the content of this block as a string """
        return "id = {} , hash = {} , prev_hash = {} , next_hash = {} , proof_no = {} , data = {}" \
            .format(self.id, self.hash, self.prev_hash, self.next_hash, self.proof_no,  self.data)

    def to_json(self):
        """ return a json string of this block """
        return json.dumps(self)

    def from_json(self, block_json):
        """ load a json string to this block """
        self = json.loads(block_json)


    def __get_time_stamp(self):
        """ Generate a timestamp """
        return int(round(time.time() * 1000))

    def __get_hash(self):
        """ generate a hash for this block using the timestamp the previous hash and the data """
        str = "{}{}{}{}".format(self.timestamp, self.prev_hash, self.data,self.proof_no)
        return henc.sha256(str.encode()).hexdigest()




