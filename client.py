import grpc

import service_pb2
import service_pb2_grpc

def main():
    host = 'localhost'
    port = 1337

    with open('server.crt', 'rb') as f:
        trusted_certs = f.read()

    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    channel = grpc.secure_channel('{}:{}'.format(host, port), credentials)

    stub = service_pb2_grpc.ServerStub(channel)
    stub.Foo(service_pb2.Empty())

    response = stub.SayHello(service_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)

    response = stub.SayHelloAgain(service_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    main()
