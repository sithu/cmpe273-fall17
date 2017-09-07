### Requirements

Implement a key-value store gRPC service using [RocksDB](https://pypi.python.org/pypi/python-rocksdb).

### 1. How to install dependency

* RocksDB native - https://github.com/facebook/rocksdb/blob/master/INSTALL.md

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. How to generate Python gRPC code from your .proto service definition.

```sh
python3 -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. datastore.proto 
```
