from socket import *

# Define server details
serverName = "127.0.0.1"
serverPort = 12000

# Create the UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Get the file name from the user
sentence = input("\nEnter file name: ")

# Send the file name to the server
clientSocket.sendto(bytes(sentence, "utf-8"), (serverName, serverPort))

# Receive the file content from the server
filecontents, serverAddress = clientSocket.recvfrom(2048)

# Print the received content from the server
print('\nReply from Server:\n')
print(filecontents.decode("utf-8"))

# Close the socket
clientSocket.close()

