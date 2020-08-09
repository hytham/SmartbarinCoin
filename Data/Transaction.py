"""
The smallest data unit that a a block in a block chain will store
"""


class Transaction(object):
    def __init__(self, sender_address, recepeaint_address,value):
        self.sender_address = sender_address
        self.recepeaint_address = recepeaint_address
        self.value = value

