import hashlib
import grpc
import token_pb2, token_pb2_grpc


def get_rendezvous_node(nodes, key):
    """
    Find the highest hash value via hash(node+key) of Rendezvous hashing and the node that generates the highest
    hash value among all nodes. You MUST use hashlib to hash the node '0.0.0.0:3000' and key combination.
        Example: 
        x = '0.0.0.0:3000' + 'key'
        x = node + key
        hash = hashlib.md5(x).hexdigest()
        Use utf-8 encoding if needed.
        @https://docs.python.org/2/library/hashlib.html
    :param nodes: a list of servers.
    :param key: a string key name.
    :return the highest node.
    """
    # TODO

    return None


class Client():
    
    def __init__(self, server):
        channel = grpc.insecure_channel(server)
        self.stub = token_pb2.TokenStub(channel=channel)
        print("Client connected to {}".format(server))


    def info(self):
        return self.stub.info(token_pb2.Empty())


    def transfer(self, symbol, from_wallet, to_wallet, amount):
        req = token_pb2.TransferRequest(symbol=symbol, fromWallet=from_wallet, toWallet=to_wallet, amount=amount)
        resp = self.stub.transfer(req)
        return resp.status


class BlockchainClient():
    
    def __init__(self, servers=None):
        self.servers = servers
        

    def transfer(self, coin_symbol, from_wallet, to_wallet, amount):
        server = get_rendezvous_node(self.servers, coin_symbol)
        client = Client(server)
        return client.transfer(coin_symbol, from_wallet, to_wallet, amount)


    def info(self, coin):
        server = get_rendezvous_node(self.servers, coin)
        client = Client(server)
        return client.info()


def test():
    coins = ['SFSU', 'SJSU', 'UCLA']
    servers = ['0.0.0.0:3000', '0.0.0.0:3001', '0.0.0.0:3002']

    for coin in coins:
        # Sending test transactions.
        print("Testing {} coin transactions".format(coin))
        blockChain = BlockchainClient(servers)
        status = blockChain.transfer(coin, "owner", "Alice", 10)
        print("{} Coin: TXN 1 - result = {}".format(coin, status))
        status = blockChain.transfer(coin, "Alice", "Bob", 5)
        print("{} Coin: TXN 2 - result = {}".format(coin, status))
        print(blockChain.info(coin))


if __name__ == '__main__':
    test()