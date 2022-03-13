"""
Sources:
https://www.geeksforgeeks.org/socket-programming-python/
https://stackoverflow.com/questions/41105735/python-print-socket-used-to-connect-to-server
https://www.journaldev.com/15906/python-socket-programming-server-client
"""

import socket

# set up server socket
host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 7777

host_name = 'localhost'

# find ip address via DNS hostname
host_ip = socket.gethostbyname(host_name)

# bind port and ip address to socket
host_socket.bind((host_ip, port))

# listen for requests
host_socket.listen()

print("Server listening on: %s, port: %d\n" %(host_name, port))

# accept client requests, print client address
client, address = host_socket.accept()

print("Connected by ", str(address))

print("Waiting for message....")

# get client initial request
request = client.recv(8192)
decoded_request = request.decode()
print("Type /q to quit\nEnter message to send...")

# until the exit code is typed, keep accepting requests with size limit 8192
while decoded_request != '/q':
  # print request
  print("Recieved: ", decoded_request)
  response = input(">")
  # send input
  client.send(response.encode())
  # receive new request
  request = client.recv(8192)
  decoded_request = request.decode()

# you will get here if client exits, then send exit code to client to close connection
response = '/q'
client.send(response.encode())
print("Client exited chat")

# close out sockets
client.close()
host_socket.close()