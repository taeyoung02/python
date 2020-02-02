import os
from chardet import detect
def search_dir(dirname):
    result_list=[]
    filenames=os.listdir(dirname)#인자에 있는 모든 파일, 디렉토리 리스트 가져옴

    for filename in filenames:
        full_path=os.path.join(dirname,filename)#경로를 병합하여 새경로 생성
        if os.path.isdir(full_path): #디렉토리이면 파일이 나올떄까지 재귀
            result_list.extend(search_dir(full_path)) #result_list는 지역변수이므로 함수가 종료되면 사라지는데,
                                                      #search_dir(full_path)를 result에 담지않으면
                                                      #재귀함수가 종료될때 사라져버림
                                                      #따라서 결과값을 받아줄 외부변수가 필요
                                                      #누적된 result_list는 최초로 호출된 지점으로 리턴
        else: #파일이면 리스트에 합침
            result_list.append(full_path)
    return result_list

def get_encoding_type(filepath):
    with open(filepath,"rb") as f:#파일을 인자로받아 바이너리로 읽음
        rawdata=f.read() #읽은것을 저장
    
    codec=detect(rawdata) #읽은것을 찾아 저장(딕셔너리로 여러정보가 나옴)
    return codec["encoding"] #encoding의 밸류만 가져옴

INCLUDE_EXT=[".txt", ".smi"]
path="c:\\python"

filelists=search_dir(path)

for file in filelists: #file = path에 있는 파일, 디렉토리명들
    filename, ext= os.path.splitext(file) #파일 확장자명 분리한것을 ext에 저장
    tempfile = filename + "_tmp" + ext

    if ext.lower() in INCLUDE_EXT:
        encoding=get_encoding_type(file)
        if encoding.lower().find("utf")<0: #utf가 아닌 인코더면
            try:
                with open(file,"r") as read, open(tempfile, "w", encoding="utf-8") as write:
                    write.write(read.read()) #file을 읽어서 tempfile에 씀(인코딩을 utf-8로 바꿈)
                os.unlink(file) #원본파일 삭제
                os.rename(tempfile,file) #임시파일명을 원본파일명으로
                print("{} is saved".format(file))
            except:
                pass
            finally:
                if os.path.exists(tempfile):
                    os.unlink(tempfile)