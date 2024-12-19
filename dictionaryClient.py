from __future__ import print_function

import logging

import grpc
import dictionary_pb2
import dictionary_pb2_grpc


def run():
    print("Starting dictionary client")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = dictionary_pb2_grpc.DictionaryStub(channel)

        # response = stub.SayHello(dictionary_pb2.HelloRequest(name='you'))
        # print("Greeter client received: " + response.message)

        # About
        response = stub.About(dictionary_pb2.EmptyRequest())
        print("About: \n" + response.text + "\n")

        # Author
        response = stub.Author(dictionary_pb2.EmptyRequest())
        print("Author: \n" + response.text + "\n")

        # AllConcepts
        response = stub.AllConcepts(dictionary_pb2.EmptyRequest())
        print("AllConcepts: \n" + str(response.definitions) + "\n")

        # List
        response = stub.List(dictionary_pb2.EmptyRequest())
        print("List: \n" + str(response.concepts) + "\n")

        # Definition
        response = stub.Definition(dictionary_pb2.DefinitionRequest(name="rpc"))
        print("Definition: rpc\n" + str(response.description) + "\n")

        # Create
        response = stub.Create(dictionary_pb2.CreateRequest(name='you', description='magnificent'))
        print("Create: you = magnificent\nStatus: " + str(response.status) + "\nMessage: " + response.message +"\n")

        # Definition
        response = stub.Definition(dictionary_pb2.DefinitionRequest(name="you"))
        print("Definition: you\n" + str(response.description) + "\n")

        # Update
        response = stub.Update(dictionary_pb2.CreateRequest(name='you', description='Are breathtaking'))
        print("Create: you = Are breathtaking\nStatus: " + str(response.status) + "\nMessage: " + response.message +"\n")

        # Definition
        response = stub.Definition(dictionary_pb2.DefinitionRequest(name="you"))
        print("Definition: you\n" + str(response.description) + "\n")

        # Remove
        response = stub.Remove(dictionary_pb2.DefinitionRequest(name="you"))
        print("Create: you\nStatus: " + str(response.status) + "\nMessage: " + response.message +"\n")

        # AllConcepts
        response = stub.AllConcepts(dictionary_pb2.EmptyRequest())
        print("AllConcepts: \n" + str(response.definitions) + "\n")




if __name__ == "__main__":
    logging.basicConfig()
    run()