from pynput.keyboard import Key, Listener, KeyCode
import keyboard
# def key_pressed(key):
#     print("Pressed {}".format(key))
    
# def key_released(key):
#     # print("Released {}".format('key'))
#     print("*",end='')
#     if key == Key.esc:
#         return False
        
# # with Listener(on_press = key_pressed,\
# #     on_release=key_released) as listener:
# #     listener.join()
# with Listener(on_release=key_released) as listener:
#     listener.join()
import curses
import os

def main(win):
    win.nodelay(True)
    key=""
    win.clear()                
    win.addstr("Detected key:")
    while 1:          
        try:                 
           key = win.getkey()         
           win.clear()                
           win.addstr("Detected key:")
           win.addstr(str(key)) 
           if key == os.linesep:
              break           
        except Exception as e:
           # No input   
           pass         
main()