import grpc
import replicator_pb2
import replicator_pb2_grpc
import uuid
from concurrent import futures

class ReplicatorServer(replicator_pb2.ReplicatorServicer):
    def __init__(self, db):
        self.db = db

    def send(self, request, context):
        print(request)
        if request.cmd == 1:
            self.db.put(request.argument)
        elif request.cmd == 2:
            self.db.delete(request.argument)
        else:
            replicator_pb2.Response(result=False)

        return replicator_pb2.Response(result=True)


def start_replicator_server(host, port, db):
    '''
    Run the GRPC Replicator listener server
    '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    replicator_pb2_grpc.add_ReplicatorServicer_to_server(ReplicatorServer(db), server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()
    return server
