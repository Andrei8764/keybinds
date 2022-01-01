from pynput import keyboard

def on_press(key):
    print(key)
    try:
        k = key.char
    except:
        k = key.name
    print(k)
    if k == 'esc':
        return False

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()