'''
################################## server.py #############################
# gRPC Replicator Server 
################################## server.py #############################
'''
import time
import grpc
import replicator_pb2
import replicator_pb2_grpc
import uuid
#import rocksdb

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class ReplicatorServer(replicator_pb2.ReplicatorServicer):
    def __init__(self):
        print("init")
        #self.db = rocksdb.DB("lab1.db", rocksdb.Options(create_if_missing=True))

    def put(self, request, context):
        print("put")
        key = uuid.uuid4().hex
        # TODO - save key and value into DB converting request.data string to utf-8 bytes 
        
        return replicator_pb2.Response(data=key)

    def get(self, request, context):
        print("get")
        # TODO - retrieve the value from DB by the given key. Needs to convert request.data string to utf-8 bytes. 
        value = uuid.uuid4().hex

        return replicator_pb2.Response(data=value)

    def send(self, request, context):
        print(request)
        return replicator_pb2.Response(result=True)


def start_replicator_server(host, port):
    '''
    Run the GRPC Replicator listener server
    '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    replicator_pb2_grpc.add_ReplicatorServicer_to_server(ReplicatorServer(), server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()
    return server
