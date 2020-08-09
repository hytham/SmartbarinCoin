"""
CLI to communicate to teh spart brain coin network
"""
import grpc

from Net.gRPC import smartbraincoin_pb2, smartbraincoin_pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = smartbraincoin_pb2_grpc.GreeterStub(channel)
  response = stub.SayHello(smartbraincoin_pb2.PingRequest(name='you'))
  print("Greeter client received: " + response.message)
  response = stub.SayHelloAgain(smartbraincoin_pb2.HelloRequest(name='you'))
  print("Greeter client received: " + response.message)