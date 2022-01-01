
# Author: Andrei9876
# Discord: Andrei9876#6160

import json
import os.path

file_exist2s = os.path.exists('.env')
if file_exist2s == False:
    config = {"dependency_installed": '', "debug_mode": ''}
    json_object = json.dumps(config, indent = 3)
    with open(".env", "w") as outfile:
        outfile.write(json_object)
def code():
    import pyautogui, pydirectinput
    from pynput import keyboard
    from time import sleep
    import os

    # Setup #
    file_exists = os.path.exists('config.json')
    if file_exists == False:
        print(" ________________________________________________________________")
        print("|                                                                |")
        print("|                          Config Setup                          |")
        print("|                                                                |")
        print("|________________________________________________________________|")
        print("")
        print("")
        snaks_key = input("Snaks Key: ")
        exit_key = input("Exit Key: ")
        if snaks_key == '' or exit_key == '':
            print("Sorry but you can t leave empty!")
            sleep(0.5)
            print("Press any key to exit.")
            input()
            os.system('cls')
            code()
        config = {
            "snaks_key": snaks_key,
            "armour_key": "",
            "exit_key": exit_key
        }
        json_object = json.dumps(config, indent = 3)
        with open("config.json", "w") as outfile:
            outfile.write(json_object)

    else:    
        with open("config.json", "r") as config:
            data = json.load(config)
            snaks_key = data["snaks_key"]
            armour_key = data["armour_key"]
            exit_key = data["exit_key"]
        keydelay = 0.25
        def snaks():
            pydirectinput.keyDown('m')
            pydirectinput.keyUp('m')
            sleep(0.120)
            for i in range(2):
                pydirectinput.keyDown('down')
                pydirectinput.keyUp('down')
                sleep(keydelay)
            pydirectinput.keyDown('enter')
            pydirectinput.keyUp('enter')
            sleep(keydelay)
            for i in range(4):
                pydirectinput.keyDown('down')
                pydirectinput.keyUp('down')
                sleep(keydelay)
            pydirectinput.keyDown('enter')
            pydirectinput.keyUp('enter')
            sleep(keydelay)
            for i in range(3):
                pydirectinput.keyDown('enter')
                pydirectinput.keyUp('enter')
                sleep(keydelay)
            for i in range(3):
                pydirectinput.keyDown('backspace')
                pydirectinput.keyUp('backspace')
                sleep(keydelay)

        def on_press(key):
            try:
                k = key.char
            except:
                k = key.name
            if k == snaks_key:
                snaks()
                print('Snaks was be added!')
            if k == exit_key or str(key) == "'\x03'":
                return False

        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        listener.join()

def install_setup():
    import os
    os.system('cls')
    print('Press any key to start installation setup!')
    os.system('pip install pynput')
    os.system('pip install PyDirectInput')
    os.system('pip install pyautogui')
    os.system('cls')
    print('Dependency was installed with success!')
    print('Press enter to restart the application!')
    input()
    os.system('cls')
    config = {"dependency_installed": 'yes', "debug_mode": 'no'}
    json_object = json.dumps(config, indent = 3)
    with open(".env", "w") as outfile:
        outfile.write(json_object)
    code()
    

try:
    code()
except:
    with open(".env", "r") as config:
        data = json.load(config)
        dependency_installed = data["dependency_installed"]
    if dependency_installed == 'yes':
        exit()
    else:
        install_setup()
