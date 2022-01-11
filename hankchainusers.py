from hankchainuser import HankChainUser
from hankchaintransaction import HankChainTransaction
from hankchainblock import HankChainBlock
from hankchain import HankChain

class HankChainUsers:
    def __init__(self):
        self._users = []

    def new_user(self, user):
        for existing_user in self._users:
            if existing_user.get_username() == user.get_username():
                print("User already exists. Failed to add account")
                return
        self._users.append(user)

    def login(self, username, password):
        userExists = False
        for user in self._users:
            if user.get_username() == username:
                userExists = True
                if user.login(password):
                    print("login successful")
                else:
                    print("login failed")
        if userExists == False:
            print("User does not exist.")

    def get_user(self, username):
        for user in self._users:
            if user.get_username() == username:
                return user
        print("User does not exist.")
        return None

    def print_users(self):
        for user in self._users:
            print(user.get_username())
