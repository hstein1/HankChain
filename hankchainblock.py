import hashlib
from hankchaintransaction import HankChainTransaction
from hankchainuser import HankChainUser

class HankChainBlock:
    
    def __init__(self, previous_hash, transactions):
        self._previous_hash = previous_hash
        self._transactions = transactions
        self._hashed_transactions = self.transaction_hash()
        self._hash = self.block_hash()
        self._validity = False

    def block_hash(self):
        hash_str = self._previous_hash + "," + ",".join(self._hashed_transactions)
        return hashlib.sha256(hash_str.encode()).hexdigest()

    def get_hash(self):
        return self._hash

    def transaction_hash(self):
        hashed_trans = []
        for trans in self._transactions:
            hashable_trans = trans.get_hashable()
            hashed_trans.append(hashlib.sha256(hashable_trans.encode()).hexdigest())
        return hashed_trans

    def update_balances(self):
        for trans in self._transactions:
            trans.check_validity()
            if trans.get_validity() == True:
                snd = trans.get_sender()
                rcv = trans.get_receiver()
                amt = trans.get_amount()
                snd.withdraw(amt)
                rcv.deposit(amt)

    def get_validity(self):
        return self._validity

    def set_validity(self, validity):
        self._validity = validity
