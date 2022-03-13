"""
Sources used: 

https://www.geeksforgeeks.org/socket-programming-python/
https://www.geeks3d.com/hacklab/20190110/python-3-simple-http-request-with-the-socket-module/
https://stackoverflow.com/questions/14591226/python-socket-and-measuing-bytes-received
https://docs.python.org/3/howto/sockets.html
"""

import socket

# create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# initialize host port 80 for HTTP requests
host_port = 7777

host_name = 'localhost'

# find ip address via DNS hostname
host_ip = socket.gethostbyname(host_name)

# set up initial TCP connection
client_socket.connect((host_ip, host_port))

print("Connected to: %s, port: %d\n" %(host_name, host_port))

# send request to host
print("Type /q to quit\nEnter message to send...")

decoded_response = None

# until the exit code is typed, keep accepting requests with size limit 8192
while decoded_response != '/q':
  # wait for response after initial request, then keep going back and forth
  if decoded_response:
    print("Received: ", decoded_response)
  request = input(">")
  # send input
  client_socket.send(request.encode())
  # receive response from server
  response = client_socket.recv(8192)
  decoded_response = response.decode()

# you will get here if server exits, then send exit code to server to close connection
request = '/q'
client_socket.send(request.encode())
print("Server exited chat")

#close sockets
client_socket.close()
