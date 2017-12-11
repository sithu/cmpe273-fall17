import grpc
import replicator_pb2_grpc
import replicator_pb2

class ReplicatorClient():
    
    def __init__(self, port, host='0.0.0.0'):
        channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = replicator_pb2_grpc.ReplicatorStub(channel)

    def send(self, data):
        response = self.stub.send(replicator_pb2.Request(data=data))
        return response.data
