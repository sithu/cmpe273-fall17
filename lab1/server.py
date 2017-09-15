'''
################################## server.py #############################
# 
################################## server.py #############################
'''
import time
import grpc
import datastore_pb2
import datastore_pb2_grpc

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class MyDatastoreServicer(datastore_pb2.DatastoreServicer):
    '''
    '''

    def __init__(self):
        '''
        '''
        # TODO
        print("init")

    def put(self, request, context):
        '''
        '''
        # TODO
        print("put")
        return None

    def get(self, request, context):
        '''
        '''
        # TODO
        print("get")
        return None

def run(host, port):
    '''
    Run the GRPC server
    '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    datastore_pb2_grpc.add_DatastoreServicer_to_server(MyDatastoreServicer(), server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()

    try:
        while True:
            print("Server started at...%d" % port)
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run('0.0.0.0', 3000)