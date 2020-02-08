import tkinter#내장 모듈
import socket
from threading import Thread

IP=""
PORT=0

def recv_message(sock):
    while True:
        msg=sock.recv(1024)
        chat_list.insert(tkinter.END, msg.decode())#맨마지막출에 채팅추가
        chat_list.see(tkinter.END)#채팅오면 맨 마지막으로 스크롤해줌
    
#주소를 구해서 연결함
def connect(event=None):
    global IP, PORT
    connect_string=input_string.get()#str형태의 문자열반환
    #ip와 포트 분리
    addr=connect_string.split(":")
    IP=addr[0]
    PORT=int(addr[1])
    window.destroy()


def send_msg(event=None):
    name=input_name.get()
    sock.send(name.encode())
    input_name.set("")#메시지 초기화

    msg=input_msg.get()
    sock.send(msg.encode())
    input_msg.set("")
    if msg=="/bye":
        sock.close()
        window.quit()
    pass

#tkinter는 라벨, 엔트리(입력하는곳), 버튼으로 이루어짐
window= tkinter.Tk()
window.title("접속대상")#창 이름
#라벨
tkinter.Label(window, text="접속대상").grid(row=0, column=0)#라벨 위치 0,0
input_string=tkinter.StringVar(value="127.0.0.1:12000")
#엔트리 박스를 만들어서 저장
input_addr=tkinter.Entry(window, textvariable=input_string, width=20)
input_addr.grid(row=0,column=1)#엔트리위치 0,1
#버튼. 누르면 실행되도록
c_button=tkinter.Button(window, text="접속하기",command=connect)
c_button.grid(row=0, column=2, padx=5, pady=5)#pad가 여백을 줌, 버튼위치 0,2
#gird함수로 위치지정

#창 크기지정
width=300
height=45

screen_width=window.winfo_screenwidth()#창의 넓이
screen_height=window.winfo_screenheight()#창의 높이

x=screen_width//2-width//2
y=screen_height//2-height//2
window.geometry('{}x{}+{}+{}'.format(width,height,x,y ))#창의 위치를 정해줌
window.mainloop()


'''채팅창 만들기'''
window=tkinter.Tk()
window.title("클라이언트")

frame=tkinter.Frame(window)
scroll=tkinter.Scrollbar(frame)
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

#프레임(채팅창)을 창에 패킹
chat_list=tkinter.Listbox(frame, height=15, width=50, yscrollcommand=scroll.set)
chat_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH, padx=5, pady=5)
frame.pack()

input_msg=tkinter.StringVar()
#채팅입력박스
send_button=tkinter.Button(window, text="전송", command=send_msg)
send_button.pack(side=tkinter.RIGHT, fill=tkinter.X, padx=5, pady=5)

inputbox=tkinter.Entry(window, textvariable=input_msg)
inputbox.bind("<Return>",send_msg)#return(enter)키가 눌리면 send_msg실행
#side=tkinter.LEFT: 왼쪽정렬,  fill=tkinter.BOTH: 양쪽 화면을 채움, expand=tkinter.YES: 창 확장가능
inputbox.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=tkinter.YES, padx=5, pady=5)


input_name=tkinter.StringVar()
#닉네임입력박스
name_inputbox=tkinter.Entry(window, textvariable=input_name)
name_inputbox.bind("<Return>",send_msg)
name_inputbox.pack(side=tkinter.TOP, fill=tkinter.X, padx=3, pady=5)

name_button=tkinter.Button(window, text="닉네임 사용", command=send_msg)
name_button.pack(side=tkinter.TOP, fill=tkinter.X, padx=3, pady=5)

sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP,PORT))

#쓰레드
th=Thread(target=recv_message, args=(sock,))
th.daemon=True
th.start()

window.mainloop()

