from hankchainuser import HankChainUser
from hankchaintransaction import HankChainTransaction
from hankchainblock import HankChainBlock
from hankchain import HankChain

hc_genesis = HankChainBlock("GENESIS", [])
hc = HankChain(hc_genesis)

hc.print_blocks()

hank = HankChainUser("hankstein", "password")
hank.deposit(5000)

satoshi = HankChainUser("satoshi", "bitcoin")
satoshi.deposit(5000)

vitalik = HankChainUser("vitalik", "ethereum")
vitalik.deposit(5000)

t1 = HankChainTransaction(hank, satoshi, 350)
t2 = HankChainTransaction(vitalik, hank, 130)


b1 = HankChainBlock(hc_genesis.get_hash(), [t1, t2])

hc.add_block(b1)

hc.print_blocks()

t3 = HankChainTransaction(hank, vitalik, 5000)
t4 = HankChainTransaction(hank, satoshi, 100)

b2 = HankChainBlock(b1.get_hash(), [t3, t4])

hc.add_block(b2)

hc.print_blocks()
