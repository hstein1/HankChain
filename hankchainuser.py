class HankChainUser:
    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._balance = 0
        self._transactions = []

    def set_password(self, password):
        self._password = password

    def get_balance(self):
        return self._balance

    def get_transactions(self):
        return self._transactions

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_username(self):
        return self._username

    def login(self, password):
        if self._password == password:
            return True
        else:
            return False
