import pyautogui
import time

# Exibe uma caixa de diálogo com a pergunta
response = pyautogui.confirm('Podemos começar os likes?')

if response == 'OK':
    while True:
        pyautogui.click(1775, 757)  # Clica na posição especificada (1826, 804)
        time.sleep(1)  # Aguarda 3 segundos
