import socketserver

class MyHandler(socketserver.BaseRequestHandler):
    users={}
    
    def send_all_message(self, msg):#클라이언트들에게 메시지 전송
        for sock, addr in self.users.values():#밸류엔 소켓과 주소가 저장되있음
            sock.send(msg.encode())#메세지 바이트로 암호화. 메시지 전송시엔 컴퓨터가 알아들을수 있도록 해줘야함.

    def handle(self):
        print(self.client_address)
        while True:
            self.request.send("채팅 닉네임을 입력하세요.".encode())
            nickname=self.request.recv(1024).decode()
            if nickname in self.users:
                self.request.send("이미 등록된 닉네임입니다.\n".encode())
            else:
                self.users[nickname]=(self.request, self.client_address)#request=소켓. 소켓과 주소를 튜플로 키에 저장
                print("현재 {}명 참여중".format(len(self.users)))
                self.send_all_message("[{}] 님이 입장 했습니다.".format(nickname))
                break
        cnt=0
        while True:#채팅을 주고받음
            if cnt==0:
                cnt+=1
                continue
            msg=self.request.recv(1024)
            if msg.decode()=="/bye":
                self.request.close()
                break
            self.send_all_message("[{}]: {}".format(nickname,msg.decode()))

        if nickname in self.users:#/bye로 빠져나가면 유저목록에서 삭제
            del self.users[nickname]
            self.send_all_message("[{}] 님이 퇴장하셨습니다.".format(nickname))
            print("현재 {}명 참여중".format(len(self.users)))


class ChatServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

server=ChatServer(("",12000),MyHandler)
server.serve_forever()
server.shutdown()
server.server_close()
