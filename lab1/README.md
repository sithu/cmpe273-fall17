### Requirements

Implement a key-value store gRPC service using [RocksDB](https://pypi.python.org/pypi/python-rocksdb).

### 1. How to run Python scripts via Docker

* RocksDB native - https://github.com/facebook/rocksdb/blob/master/INSTALL.md
* gRPC Docker - https://github.com/grpc/grpc-docker-library/tree/master/1.4/python
 
```sh
# Generate Stub for client and server
$ docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp grpc/python:1.4 python3 -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. datastore.proto


# Server
$ docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp grpc/python:1.4 python3 server.py

# Client
$ docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp grpc/python:1.4 python3 client.py

```

### 2. How to generate Python gRPC code from your .proto service definition.

```sh
python3 -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. datastore.proto 
```

### 3. Run the server

```sh
python3 server.py
```

### 4. Run the client

```sh
python3 client.py
```