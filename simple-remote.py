#!/usr/bin/python3
#
#This is a script to introduce networking to the simple-write exploitable
# program.
#
# DO NOT RUN ON A PUBLIC NETWORK!


import socket
import subprocess

# SOCKET SETUP
HOST = "127.0.0.1"
PORT = 31337

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Listening on {HOST}:{PORT}")

client_socket, client_address = server_socket.accept()
print(f"Got connection from {client_address}")
client_socket.sendall(b">>> ")

with client_socket:
    input_string = client_socket.recv(2048)
    # RUN PROCESS
    command = ["./simple-write"]
    subprocess.run(command, input=input_string)
    client_socket.sendall(b"input received")
    client_socket.close()



