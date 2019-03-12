class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []


    def new_blockchain(self):
        # Creasts a new Block and adds it to the chain
        pass


    def new_transaction(self, sender, recipient, amount):
        # Adds a new transation to the list of transactions
        ""
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the block that will hold this transaction
        ""

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # Hashes a Block
        pass

    @property
    def last_block(self):
        # Returns the last block in the chain
        pass

