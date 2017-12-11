
```sh
python3 -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. replicator.proto
```

https://github.com/grpc/grpc.github.io/blob/master/docs/tutorials/basic/python.md

# How to run a node

```sh
python3 app.py 4000 3000
```

# How to run a peer

```sh
python3 app.py 3000 4000
```
