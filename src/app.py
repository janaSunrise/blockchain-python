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
    return "We'll mine a new Block"


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
