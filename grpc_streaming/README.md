# Compile the proto IDL

```sh
python3 -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. echo.proto
```

- [GRPC Streaming](https://github.com/grpc/grpc.github.io/blob/master/docs/tutorials/basic/python.md)

# Run the server

```sh
python3 server.py
```

# Run the client

```sh
python3 client.py
```
