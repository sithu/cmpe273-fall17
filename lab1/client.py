'''
################################## client.py #############################
# 
################################## client.py #############################
'''
import grpc
import datastore_pb2

class DatastoreClient():
    '''
    '''

    def __init__(self, host='0.0.0.0', port=3000):
        '''
        '''
        # TODO
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = datastore_pb2.DatastoreStub(self.channel)

    def put(self, data):
        '''
        '''
        # TODO
        return None # self.stub.put(req)

    def get(self, id):
        '''
        '''
        # TODO
        return None # self.stub.get(req)


print("Client is running...")
client = DatastoreClient()
# TODO 
# resp = client.put(req)
# resp = client.get(req)
