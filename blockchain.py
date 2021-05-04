from hashlib import sha256
from datetime import datetime

# calcul du hash d'un bloc
def calculHash(block):
    bloc = str(block.index) + str(block.previousHash) + str(block.timestamp) + str(block.data) + str(block.nonce)
    return(sha256(bloc.encode('utf-8')).hexdigest())

# création de la  Blockchain


class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.blocks = []
        genesisBlock = Block(0, None, datetime.now(), "Genesis block")
        genesisBlock.mineBlock(self.difficulty)
        self.blocks.append(genesisBlock)

 # création de la classe  Block
class Block(object):
    def __init__(self, index, previousHash, timestamp, data):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.nonce = 0
        self.hash = calculHash(self)

    def createBlock(self, difficulty):
        zeros = repeat("0", difficulty)

        while self.hash[0:difficulty] != zeros:
            self.nonce = self.nonce + 1
            self.hash = calculHash(self)