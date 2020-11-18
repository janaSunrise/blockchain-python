class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        
    def new_block(self):
        """
        Creates a new Block and adds it to the chain.
        """
        pass
    
    def new_transaction(self, sender: str, recipient: str, amount: int):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        self.current_transactions.append(
            {
                'sender': sender,
                'recipient': recipient,
                'amount': amount,
            }
        )
    
    @staticmethod
    def hash(block):
        """
        Hashes a Block.
        """
        pass

    @property
    def last_block(self):
        """
        Returns the last Block in the chain.
        """
        pass