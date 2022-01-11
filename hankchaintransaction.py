import hashlib
from hankchainuser import HankChainUser

class HankChainTransaction:

    def __init__(self, sender, receiver, amount):
        self._sender = sender
        self._receiver = receiver
        self._amount = amount
        self._validity = True
        self._hashable_trans = self.hashable_trans()

    def set_validity(self, validity):
        self._validity = validity

    def get_validity(self):
        return self._validity
    
    def check_validity(self):
        if self._sender.get_balance() < self._amount:
            print("Not enough money")
            self.set_validity(False)

    def get_sender(self):
        return self._sender

    def get_receiver(self):
        return self._receiver

    def get_amount(self):
        return self._amount

    def hashable_trans(self):
        return self._sender.get_username() + "," + self._receiver.get_username() + "," + str(self._amount)

    def get_hashable(self):
        return self._hashable_trans

    
