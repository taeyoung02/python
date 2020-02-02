import socket
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
google_ip=socket.gethostbyname("google.com")#dns서버: 도메인을 ip로 변환
sock.connect((google_ip, 80))

sock.send("GET / HTTP/1.1\n".encode())#바이트로 인코딩
sock.send("\n".encode())

buffer = sock.recv(4096)
buffer = buffer.decode().replace("\r\n","\n")
sock.close()

print(buffer)
#세션 - 정보가 서버에 저장됨
#쿠키 - 정보가 내 컴퓨터에 저장됨