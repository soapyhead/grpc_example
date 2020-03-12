# gRPC Example

1. Create calculator.py
2. Define interface in calculator.proto
3. Generate gRPC stuff
```bash
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. calculator.proto
```
4. Implement server.py
```bash
python server.py
```
5. Implement client.py
```bash
python client.py
```