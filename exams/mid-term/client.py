'''
################################## client.py #############################
# This Encoder Client invokes a remote GRPC service to encode and decode
# from a string URL to an integer value back and forth.
################################## client.py #############################
'''
import grpc
import encoder_pb2

class EncoderClient():
    '''
    EncoderClient is a proxy to GRPC EncoderServer.
    '''

    def __init__(self, host='0.0.0.0', port=3000):
        '''
        Initializes GRPC channel and encoder stud.
        '''
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = encoder_pb2.EncoderStub(self.channel)

    def encode(self, _url):
        '''
        Encode a given _url string.
        '''
        req = encoder_pb2.EncodeRequest(url=str(_url))
        return self.stub.encode(req)

    def decode(self, _id):
        '''
        Decode a given _id integer.
        '''
        req = encoder_pb2.DecodeRequest(id=int(_id))
        return self.stub.decode(req)

def test():
    client = EncoderClient()
    url = 'goog'
    resp = client.encode(url)
    id = resp.id
    print("Encode URL={}: id={}".format(url, id))

    resp = client.decode(id)
    print("Decode id={}: URL={}".format(id, resp.url))


if __name__ == '__main__':
    test()