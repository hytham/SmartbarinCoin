from Net.P2P import P2PNode


class smartBrainCoin:
    def __init__(self,config):
        self.p2p = P2PNode()
        self.p2p.setup()

    def start(self):
        self.p2p.mainloop()



