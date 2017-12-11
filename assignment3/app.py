#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from server import start_replicator_server
from client import ReplicatorClient

def get_input(cmd):
    if cmd == 'put':
        return cmd
    else:
        return cmd

def run_forever(host, server_port, peer_port):
    server = start_replicator_server(host, int(server_port))
    client = ReplicatorClient(int(peer_port), host)
    print("Replicator Server started at...{}".format(server_port))
    try:
        while True:
            i = input("\nEnter 'q' to quit: \n_db_>")
            if i == "q": break
            resp = client.send(get_input(i))
            print('Peer Response={}'.format(resp))
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("server_port", help="Server port")
    parser.add_argument("peer_port_list", help="Comma-separated peer ports")
    args = parser.parse_args()
    run_forever('0.0.0.0', args.server_port, args.peer_port_list)