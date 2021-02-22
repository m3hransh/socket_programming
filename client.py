import socket

server_name = '127.0.0.1'
server_port = 65123

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    message = input('Enter the word: ')
    s.sendto(message.encode(), (server_name, server_port))
    modified_message, server_addr = s.recvfrom(2048)
    print(modified_message.decode())
    s.close()