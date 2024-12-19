from concurrent import futures
import logging

import grpc
import dictionary_pb2
import dictionary_pb2_grpc

myDictionary = {
    'python': 'A high-level, interpreted programming language known for its readability and versatility.',
    'docker': 'A platform that enables developers to automate the deployment of applications inside lightweight, portable containers.',
    'docker image': 'A lightweight, standalone, and executable package that includes everything needed to run a piece of software, including code, runtime, libraries, and dependencies.',
    'docker container': 'A runtime instance of a Docker image, representing a running application in an isolated environment.',
    'devops': 'A set of practices that combines software development and IT operations to shorten the development lifecycle and improve software delivery.',
    'api': 'An interface that allows different software applications to communicate and interact with each other.',
    'rpc': 'A protocol that allows a program to execute code on another machine as if it were a local function call.'
}

class Dictionary(dictionary_pb2_grpc.DictionaryServicer):
    # def SayHello(self, request, context):
    #     return dictionary_pb2.HelloReply(message="Hello, %s!" % request.name)

    def About(self, request, context):
        return dictionary_pb2.LineReply(text="This is a dictionary with some definitions. You can modify them")

    def Author(self, request, context):
        return dictionary_pb2.LineReply(text="I am mfatov and I made this...")

    def AllConcepts(self, request, context):
        return dictionary_pb2.AllConceptsReply(definitions=myDictionary)

    def List(self, request, context):
        responseDict = {}
        counter = 1
        for item in myDictionary.keys():
            responseDict[counter] = item.capitalize()
            counter += 1
        return dictionary_pb2.ListReply(concepts=responseDict)

    def Definition(self, request, context):
        return dictionary_pb2.DefinitionReply(description=myDictionary[request.name])

    def Create(self, request, context):
        myDictionary[request.name.lower()] = request.description
        return dictionary_pb2.CompleteReply(status=200, message=f'Successfully added your definition of {request.name.capitalize()}')

    def Update(self, request, context):
        myDictionary[request.name.lower()] = request.description
        return dictionary_pb2.CompleteReply(status=200, message=f'Successfully changed definition of {request.name.capitalize()}')

    def Remove(self, request, context):
        myDictionary.pop(request.name.lower())
        return dictionary_pb2.CompleteReply(status=200, message=f'{request.name.capitalize()} successfully removed from dictionary')


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dictionary_pb2_grpc.add_DictionaryServicer_to_server(Dictionary(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()