class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []


    def new_blockchain(self):
        # Creasts a new Block and adds it to the chain
        pass


    def new_transaction(self):
        # Adds a new transation to the list of transactions
        pass

    @staticmethod
    def hash(block):
        # Hashes a Block
        pass

    @property
    def last_block(self):
        # Returns the last block in the chain
        pass

    