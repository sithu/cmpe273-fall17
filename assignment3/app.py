#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from server import start_replicator_server
from client import ReplicatorClient

def get_input(input):
    tokens = input.split()
    if len(tokens) != 2: return None, None
    cmd, arg = tokens
    if cmd == 'put' or cmd == 'delete':
        return cmd, arg
    else:
        return None, None

def run_forever(host, server_port, peer_port):
    server = start_replicator_server(host, int(server_port))
    client = ReplicatorClient(int(peer_port), host)
    print("Replicator Server started at...{}".format(server_port))
    try:
        while True:
            i = input("\nEnter 'q' to quit: \n_db_>")
            if i == "q": break
            cmd, arg = get_input(i)
            if not cmd: continue
            resp = client.send(cmd, arg)
            print('Peer Response={}'.format(resp))
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("server_port", help="Server port")
    parser.add_argument("peer_port_list", help="Comma-separated peer ports")
    args = parser.parse_args()
    run_forever('0.0.0.0', args.server_port, args.peer_port_list)