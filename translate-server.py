import socket

HOST = '127.0.0.1'
PORT = 65123
trans_map ={
    'Hello':'سلام'
}
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print('sever is ready to receive')
    while True:
        message,client_addr = s.recvfrom(2048)
        modified_message = trans_map[message.decode()].encode()
        s.sendto(modified_message, client_addr)
