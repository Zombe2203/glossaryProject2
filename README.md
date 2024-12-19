# How to run
To run this project install `gRPC`: 
```
python -m pip install grpcio
python -m pip install grpcio-tools
```
Then run command `python dictionaryServer.py` from repository root to start server.<br>
Then run command `python dictionaryClient.py` from repository root to start client. Currently it provides no user interface and just runs predetermined set of commands. All commands usages are listed in the corresponding file, feel free to change it to try other commands.<br>
Keep in mind that all changes you make will not be saved after server is disabled as this version of project does not support database integration.

