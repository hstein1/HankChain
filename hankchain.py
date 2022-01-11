from hankchainuser import HankChainUser
from hankchaintransaction import HankChainTransaction
from hankchainblock import HankChainBlock
import hashlib

class HankChain:
    def __init__(self, genesis_block):
        self._genesis_block = genesis_block
        self._users = []
        self._blocks = [genesis_block]

    def validate_block(self, new_block):
        last_hash = self._blocks[-1].get_hash()
        test_hash_str = last_hash + "," + ",".join(new_block.transaction_hash())
        test_hash = hashlib.sha256(test_hash_str.encode()).hexdigest()
        if test_hash == new_block.get_hash():
            new_block.set_validity(True)
        else:
            new_block.set_validity(False)
        
    def add_block(self, new_block):
        self.validate_block(new_block)
        if new_block.get_validity():
            self._blocks.append(new_block)
            new_block.update_balances()
            
    def print_blocks(self):
        for block in self._blocks:
            prt = "BLOCK: " + block.get_hash()
            print(prt)

    def get_prev_hash(self):
        return self._blocks[-1].get_hash()
