# SSL and server-side authentication for gRPC

This repository provides a simple example of using SSL and server-side authentication for gRPC using Python.

Python 2.7 and 3.6

gRPC: 1.9.1

For more details, see http://www.sandtable.com/using-ssl-with-grpc-in-python/

## Certificate

Generate certificate for the server. Uses `openssl`.


```
make gen_key
```
* describe CN as localhost

## Install gRPC packages

```
pip install -r requirements.txt
```

## Generate gRPC stubs

```
make stubs
```

## Run server

```
make server
```

## Run client

```
make client
```
