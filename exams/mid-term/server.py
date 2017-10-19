'''
################################## server.py #############################
# Encoder Server encodes string and decodes integer back to the original
# string. It can be used to generate unique id for a given URL.
################################## server.py #############################
'''
import time
import grpc
import encoder_pb2
import encoder_pb2_grpc

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class EncoderServer(encoder_pb2.EncoderServicer):
    '''
    EncoderServer is the main class that handles encoding and decoding.
    '''

    def __init__(self):
        print("init")

    def encode(self, request, context):
        '''
        :return: encoder_pb2.EncodeResponse
        '''
        # TODO
        print("Encode:\n", request)
        return None

    def decode(self, request, context):
        '''
        :return: encoder_pb2.DecodeResponse
        '''
        # TODO
        print("Decode:\n", request)
        return None

def run(host, port):
    '''
    Run the GRPC server
    '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    encoder_pb2_grpc.add_EncoderServicer_to_server(EncoderServer(), server)
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
