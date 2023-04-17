def startServer()
    HOST, PORT = "", 12345 
    # HOST = server_sock.gethostname()
    server_sock.bind((HOST, PORT)) 
    server_sock.listen(1) 
    sock, addr = server_sock.accept()

    while True:
        data = sock.recv(1024)  # Receive    
        data = data.upper()  # Process bytes    
        sock.sendall(data)  # Send
