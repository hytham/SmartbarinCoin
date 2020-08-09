#Smart Brain Coin

Smart Brain Coin (SBC) is new crypto-currancy intended for eduction and learning purpos
mostly for my self to understand how blockchain work. and not intended 
for production

It is written purly in python with no external library

#Implmentation steps
* Block class and the chain class [Complete]
* P2P Network [In Progress]
* Minor functionality
* Web-hocks to add to initate a transaction


# to generate an gRPC
`
python -m grpc.tools.protoc -IProtos --python_out=gRPC --grpc_python_out=gRPC smartbraincoin.proto
`