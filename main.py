import hashlib
from datetime import datetime

class Block():
    def __init__(self, datetime, metadata, previous_hash):
        self.datetime = datetime
        self.metadata = metadata
        self.previous_hash = previous_hash
        self.increate_count = 0
        self.hash = ""
        self.block_minning()

    def calculate_hash(self):
        """Calculate the hash of the block using SHA-256."""
        # block_string = f"{self.datetime}{self.metadata}{self.increate_count}{self.previous_hash}".encode()
        block_string = "{}{}{}{}".format(self.datetime,
                                         self.metadata,
                                         self.increate_count,
                                         self.previous_hash).encode()
        return hashlib.sha256(block_string).hexdigest()

    def block_minning(self, difficulty=4):
        """Perform mining on the block."""
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.increate_count += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash} with difficulty {difficulty} and increment count {self.increate_count}")

class Blockchain():
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def datetime(self):
        """Return the current datetime."""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def create_genesis_block(self):
        """Create the first block in the blockchain."""
        genesis_block = Block("2025-08-08 00:00:00", "Genesis Block", "0")
        self.chain.append(genesis_block)

    def add_block(self, metadata):
        """Add a new block to the blockchain."""
        previous_block = self.chain[-1]
        new_block = Block(self.datetime(), metadata, previous_block.hash)
        self.chain.append(new_block)

    def get_chain(self):
        """Return the blockchain."""
        return self.chain

    def is_chain_valid(self):
        """Check if the blockchain is valid."""
        for i in range(1, len(self.chain)):
            current_block: Block = self.chain[i]
            previous_block: Block = self.chain[i - 1]

            # Check if the hash of the current block is correct
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the previous hash matches
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

def testing_blockchain():
    """Test the blockchain functionality."""
    blockchain = Blockchain()

    # Add blocks to the blockchain
    blockchain.add_block("Block 1 Metadata")
    blockchain.add_block("Block 2 Metadata")

    # Print the blockchain
    for block in blockchain.get_chain():
        print(f"Block Hash: {block.hash}, Previous Hash: {block.previous_hash}, Metadata: {block.metadata}")

    # Validate the blockchain
    print("Is the blockchain valid ? \n", blockchain.is_chain_valid())

if __name__ == "__main__":
    testing_blockchain()
