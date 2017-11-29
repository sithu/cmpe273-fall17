import grpc
import echo_pb2_grpc
import echo_pb2
import time

PORT = 3000

class EchoClient():
    
    def __init__(self, host='0.0.0.0', port=PORT):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = echo_pb2_grpc.EchoStub(self.channel)

    def get_input(self):
        while 1:
            i = input("\nEnter 'q' to quit: \n_client_>")
            if i == "q":
                break
            
            yield echo_pb2.Message(data=i)
            time.sleep(0.1)

    def reverse(self):
        it = self.stub.reverse(self.get_input())
        try:      
            for r in it:
                print("_server_>" + r.data)
        except grpc._channel._Rendezvous as err:
            print(err)

def main():
    print("Client is connecting to Echo Server at {}:{}...".format('0.0.0.0', PORT))
    client = EchoClient(host='0.0.0.0')
    client.reverse()

if __name__ == "__main__":
    main()

