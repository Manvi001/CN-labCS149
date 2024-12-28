from socket import *
# Define server details
serverPort = 12000
# Create the UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Bind the server socket to an address and port
serverSocket.bind(("127.0.0.1", serverPort))
print("The server is ready to receive")
# Listen for incoming requests
while 1:
    # Receive the file name from the client
    sentence, clientAddress = serverSocket.recvfrom(2048)
    sentence = sentence.decode("utf-8")
     try:
        # Open and read the requested file
        file = open(sentence, "r")
        con = file.read(2048) 
        # Send the file content back to the client
        serverSocket.sendto(bytes(con, "utf-8"), clientAddress)
        print(f'\nSent contents of {sentence}')
        file.close()
    except FileNotFoundError:
        # If the file is not found, send an error message
        error_message = f"File '{sentence}' not found."
        serverSocket.sendto(bytes(error_message, "utf-8"), clientAddress)
        print(f'\nFile not found: {sentence}')
