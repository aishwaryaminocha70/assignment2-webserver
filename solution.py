# import socket module
from socket import *
# In order to terminate the program
import sys
serverPort=80
def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  #Fill in start
  serverSocket.bind(('127.0.0.1',13331))
  serverSocket.listen(1)
  print('The server is ready to server:',serverPort)
  #Fill in end

  while True:
    #Establish the connection
    connectionSocket, addr = serverSocket.accept()
    print('Ready to serve...')
   
    try:

      try:
        message = connectionSocket.recv(1024)
   #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        
        #Send one HTTP header line into socket.
        
        #Fill in start
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n')

        #Fill in end

        #Send the content of the requested file to the client
        connectionSocket.send(outputdata)


        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        # Send response message for file not found (404)
        #Fill in start
        connectionSocket.send('file not found (404)')

        #Fill in end


        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end

    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
