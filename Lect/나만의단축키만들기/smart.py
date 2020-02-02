from pynput.keyboard import Key, Listener, KeyCode
import win32api

MY_HOTKEY = [
    {"function1": {Key.ctrl_l, Key.alt_l, KeyCode(char="c")}},
    {"function2": {Key.shift, Key.ctrl_l, KeyCode(char="n")}},
    {"function3": {Key.alt_l, Key.ctrl_l, KeyCode(char="g")}}
]
def function1():
    print("function1 called")
    win32api.WinExec("calc.exe")

def function2():
    print("function2 called")
    win32api.WinExec("notepad.exe")

def function3():
    print("function3 called")
    win32api.WinExec("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

current_keys=set()

def key_pressed(key):
    for data in MY_HOTKEY: #핫키안의 딕셔너리를 data로 접근후 key와 value로 구분
        FUNCTION = list(data.keys())[0]
        KEYS = list(data.values())[0]
        
        if key in KEYS:
            current_keys.add(key)#누른 키를 저장
            if all(k in current_keys for k in KEYS):
                function= eval(FUNCTION)
                function()
    
    print(current_keys)
def key_released(key):
    current_keys.clear()
    print(current_keys)

    if key==Key.esc:
        return False

with Listener(on_press=key_pressed, on_release = key_released) as listener:
    listener.join()