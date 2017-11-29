import time
import grpc
import echo_pb2
import echo_pb2_grpc

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class MyEchoServicer(echo_pb2.EchoServicer):
    
    def reverse(self, request_iterator, context):
        for r in request_iterator:
            yield echo_pb2.Message(data=r.data[::-1])


def run(host, port):
    '''
    Run the GRPC server
    '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    echo_pb2_grpc.add_EchoServicer_to_server(MyEchoServicer(), server)
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