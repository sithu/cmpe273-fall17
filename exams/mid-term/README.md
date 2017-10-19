## Requirements

You will be porting a URL shortener service from [this example](http://www.geeksforgeeks.org/how-to-design-a-tiny-url-or-url-shortener/) into a Python GRPC service.


### 1. You can install GRPC in local or Use Docker image from the lab 1.

```sh
# http://www.grpc.io/docs/tutorials/basic/python.html
pip install grpcio-tools
```

### 2. How to generate Python gRPC code from your .proto service definition.

```sh
python3 -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. encoder.proto 
```

### 3. Implement all TODO sections in server.py


### 4. How to run the Server

```sh
python3 server.py
```

Server startup output:
```sh
Server started at...3000
```

### 5. How to test and Expected Output

```sh
$ python3 client.py
Encode URL=goog: id=1484658
Decode id=1484658: URL=goog
```
