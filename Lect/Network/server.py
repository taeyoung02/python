'''
1. 소켓생성
2. 바인딩
3. 접속대기
4. 접속수락
5. 데이터 송/수신
6. 접속종료
'''

import socket
print("1. 소켓생성")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#TCP방식

print("2. 바인딩")
sock.bind(("",12000))#안쓰는 포트 사용

print("3. 접속대기")
sock.listen()

print("4. 접속수락")
c_sock, addr = sock.accept()#리슨하고있는 소켓이 요청오면 clinet와 접속시켜서 새로운 소켓만듬
#클라이언트 대기중

print("5. 데이터 송/수신")
receive_data=c_sock.recv(1024)
print("수신된 데이터 : ", receive_data)

print("6. 접속종료")
c_sock.close()
sock.close()