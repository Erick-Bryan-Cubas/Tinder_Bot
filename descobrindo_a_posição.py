import pyautogui
import time

while True:
    x, y = pyautogui.position()  # Obtém a posição atual do mouse
    print(f'A posição atual do mouse é ({x}, {y})') # 1826 804