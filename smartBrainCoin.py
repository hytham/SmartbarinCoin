from Data.Blockchain import Blockchain as BC
from Net.Protocol import BlockChainProtocol


class smartBrainCoin:
    def __init__(self,config):
        self.p2p = BlockChainProtocol(BC)
        self.p2p.setup()


    def start(self):
        self.p2p.mainloop()



