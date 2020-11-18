from flask import Flask, jsonify, request

from configparser import ConfigParser
from uuid import uuid4

from .blockchain import Blockchain


# Initialize Flask app
app = Flask(__name__)


# Get the config for the Flask app
config = ConfigParser()
config.read('config.ini')


# Define blockchain Variables
blockchain = Blockchain()
node_identifier = str(uuid4()).replace('-', '')


@app.route('/mine', methods=['GET'])
def mine():
    # We run the proof of work algorithm to get the next proof.
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # We must receive a reward for finding the proof.
    # The sender is "0" to signify that this node has mined a new coin.
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    # Forge the new Block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    # Check that the required fields are in the POSTed data
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Create a new Transaction
    index = blockchain.new_transaction(
        values['sender'],
        values['recipient'],
        values['amount']
    )

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(
        host=config.get("DEBUG", "host"),
        port=config.getint("DEBUG", "port"),
        debug=config.getbool("DEBUG", "debug")
    )
