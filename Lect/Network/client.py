import socket
print("1. 소켓생성")
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("3. 접속시도")
sock.connect(("127.0.0.1", 12000))#루프백주소

print("5. 데이터 송/수신")
sock.sendall("Hello socket programming".encode())#바이트형태로 주고받아야함

print("6. 접속종료")
sock.close()