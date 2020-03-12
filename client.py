import logging

import grpc


import calculator_pb2
import calculator_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)

        number = calculator_pb2.Number(value=81)
        response = stub.SquareRoot(number)
        print(response.value)


if __name__ == '__main__':
    logging.basicConfig()
    run()
