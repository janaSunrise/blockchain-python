"""
The structure of a blockchain, Which is accessed like JSON or a dict.

Each new block contains within itself, the hash of the previous Block. 
This is crucial because it’s what gives blockchains immutability: 
If an attacker corrupted an earlier Block in the chain then all subsequent blocks will 
contain incorrect hashes.

Creating new Blocks
-------------------

When our Blockchain is instantiated we’ll need to seed it with a genesis block—a block with 
no predecessors. We’ll also need to add a “proof” to our genesis block which is the result of 
mining (or proof of work).

Understanding Proof of Work
---------------------------

A Proof of Work algorithm (PoW) is how new Blocks are created or mined on the blockchain.
The goal of PoW is to discover a number which solves a problem. The number must be difficult to 
find but easy to verify—computationally speaking—by anyone on the network. 
This is the core idea behind Proof of Work.
"""

# Dummy blockchain structure:
block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}
