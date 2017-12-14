from client import get_rendezvous_node

def test():
    coins = ['SJSU', 'UCLA', 'SFSU']
    servers = ['0.0.0.0:3000', '0.0.0.0:3001', '0.0.0.0:3002']
    # Generate coin->server mapping
    for coin in coins:
        server = get_rendezvous_node(servers, coin)
        print("{} coin is mapped to {}".format(coin, server))


if __name__ == '__main__':
    test()