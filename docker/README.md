### How to build a Docker Image with RocksDB and gRPC?

```sh
docker build -t ubuntu-python3.6-rocksdb-grpc:1.0 .
```

### How to run hello.py?

```sh
docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp ubuntu-python3.6-rocksdb-grpc:1.0 python3.6 hello.py

docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp ubuntu-python3.6-rocksdb-grpc:1.0 python3.6 hello-rocksdb.py
```
