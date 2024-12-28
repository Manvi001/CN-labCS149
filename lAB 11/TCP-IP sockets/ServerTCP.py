from socket import *
serverName = "127.0.0.1"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)

while 1:
    print("The server is ready to receive")
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    try:
        with open(sentence, "r") as file:
            file_contents = file.read(1024)
            connectionSocket.send(file_contents.encode())
            print(f"Sent contents of '{sentence}'")
    except FileNotFoundError:
        connectionSocket.send("File not found.".encode())
        print(f"File '{sentence}' not found.")
    connectionSocket.close()
