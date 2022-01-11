from hankchainuser import HankChainUser
from hankchaintransaction import HankChainTransaction
from hankchainblock import HankChainBlock
from hankchain import HankChain
from hankchainusers import HankChainUsers

vitalik = HankChainUser("vitalik", "ethereum")
vitalik.deposit(5000)

satoshi = HankChainUser("satoshi", "bitcoin")
satoshi.deposit(5000)

usrs = HankChainUsers()
usrs.new_user(vitalik)
usrs.new_user(satoshi)
currentUser = None
uncommitted_transactions = []
gb = HankChainBlock("GENESIS", [])
chain = HankChain(gb)

while True:
    if currentUser == None:
        createAccount = input("Welcome to Hank Chain. Would you like to sign in, create an account, or exit? ")
        if createAccount in ["Create", "create", "Create Account", "create account", "CreateAccount", "createaccount"]:
            usrnm = input("What will your username be? ")
            pswrd = input("What will your password be? ")
            new_user = HankChainUser(usrnm, pswrd)
            usrs.new_user(new_user)
            currentUser = new_user
        elif createAccount in ["signin", "Signin", "Sign In", "Sign in", "sign in", "SignIn"]:
            usrnm = input("What is your username? ")
            pswrd = input("What is your password? ")
            usrs.login(usrnm, pswrd)
            currentUser = usrs.get_user(usrnm)
        elif createAccount in ["Quit", "quit", "Exit", "exit"]:
            print("Goodbye!")
            break
    if currentUser != None:
        action = input("What would you like to do today? (balance, deposit, withdraw, send, mine, logout) ")
        if action == "balance":
            print("Your current balance is:", currentUser.get_balance())
        if action == "deposit":
            amt = input("How much would you like to deposit? ")
            currentUser.deposit(int(amt))
            print("Your new balance is", currentUser.get_balance())
        if action == "withdraw":
            amt = input("How much would you like to withdraw? ")
            if currentUser.get_balance() >= int(amt):
                currentUser.withdraw(int(amt))
            else:
                print("Insufficient funds.")
            print("Your new balance is", currentUser.get_balance())
        if action == "send":
            rcv = input("Who would you like to send to? ")
            rcv_usr = usrs.get_user(rcv)
            if rcv_usr != None:
                amt = input("How much would you like to send? ")
                trans = HankChainTransaction(currentUser, rcv_usr, int(amt))
                trans.check_validity()
                if trans.get_validity():
                    uncommitted_transactions.append(trans)
                else:
                    print("You don't have enough money to complete that transaction.")
            else:
                print("User does not exist. Sorry")
        if action == "mine":
            block = HankChainBlock(chain.get_prev_hash(), uncommitted_transactions)
            chain.add_block(block)
            uncommitted_transactions = []
        if action == "logout":
            print("Goodbye!")
            currentUser = None
    
        
