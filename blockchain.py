import hashlib
import datetime


#Creating a block element
class Block:
    BlockNum = 0
    data = None #data the block is holding 
    next = None #pointer to the next block
    hash = None #SHA256 hashing will be used for the mining
    nonce = 0 #nonce: number only used once
    previous_hash = 0x0 #storing hash id of the previous block when building a chain
    timestamp = datetime.datetime.now()


    #initialize a block
    def __init__(self,data):
        self.data = data
    
    #function used to compute hashing on the block
    def hash(self):
        h = hashlib.sha256()
        ##Hashing concatenated strings of block data
        h.update(
        str(self.nonce).encode('utf-8') + 
        str(self.data).encode('utf-8') + 
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.BlockNum).encode('utf-8')
        )
    
    def __str__(self):
        #prints the value to the block
        return("Block Hash: " + str(self.hash()) + "\nBlockNum: "+str(self.BlockNum) + "\nData: " + str(self.data))



#blockchain structure:
#>consists of blocks linked together

class Blockchain:
    #--------Vars------#
    maxNonce = 2**32 #largest number to store in a 32-bit number
    difficulty = 10 #mining difficulty to compute target hash
    target = 2 ** (256-difficulty) #target hash
    #------------------#
    #Generating the first block in the chain
    block = Block("Beginning")
    #Set the block as the head in the block chain -similar to linked list
    head = block


    #adding function to add to block chain
    def add(self, block):
        block.previous_hash = self.block.hash() #assigns the previous hash to the current hash
        block.BlockNum = self.block.BlockNum + 1 #adds to the number of blocks in the chain

        #assigning next ptr
        self.block.next = block #next ptr equals itself this is the new head
        self.block = self.block.next


    #mining allows for nodes who dont know eachother figure out the true chain of blockchain
    def mine(self, block):
        for step in range(self.maxNonce):
            #if the value of the blocks hash is less than the target value
            if int(block.hash(),16) <= self.target:#if less add to block chain and break loop
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1 #increment nonce
                #the higher the number the longer to mine





#initialize block chain:
blockchain = Blockchain()

#mine 10 blocks
for n in range(10):
    blockchain.mine(Block("Block " + str(n + 1)))

#printing out blocks in block chain
while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next