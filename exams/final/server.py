import time
import grpc
import token_pb2
import token_pb2_grpc
import uuid
import sys
from coin import Coin
from concurrent import futures


class BlockChainServer(token_pb2.TokenServicer):
    
    def __init__(self, symbols, wallets):
        self.symbols = symbols
        self.coins = {}
        for symbol in symbols:
            self.coins[symbol] = Coin(symbol, 100, wallets)


    def info(self, request, context):
        info_map = {}
        for symbol in self.symbols:
            info_map[symbol] = str(self.coins[symbol].blockchains_info())
        
        return token_pb2.InfoResponse(data=token_pb2.Data(entry=info_map))


    def transfer(self, request, context):
        symbol = request.symbol
        print("Receiving {} coins tranfer request: from={}, to={}, amount={}".format(symbol, request.fromWallet, request.toWallet, request.amount))
        status = 'INVALID_REQUEST'
        if self.coins[symbol].transfer(request.fromWallet, request.toWallet, request.amount):
            self.coins[symbol].add_txn_to_blockchain(request.fromWallet, request.toWallet, request.amount)
            status = 'SUCCESS'
        
        return token_pb2.TransferResponse(status=status)


def run_forever(symbols, wallets, host_port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    token_pb2_grpc.add_TokenServicer_to_server(BlockChainServer(symbols, wallets), server)
    server.add_insecure_port(host_port)
    server.start()
    print("Blockchain server {} started for symbols:{}".format(host_port, symbols))
    _ONE_DAY_IN_SECONDS = 60 * 60 * 24
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    total = len(sys.argv)
    if total < 3:
        print("Missing requried arguments... Example:\npython3 {} 0.0.0.0:3000 SJSU,UCLA".format(__file__))
        sys.exit(0)
    
    symbols = sys.argv[2].split(',')
    
    wallets = {
        "Alice": 0,
        "Bob": 0 
    }
    host_port = sys.argv[1]
    run_forever(symbols, wallets, host_port)
 