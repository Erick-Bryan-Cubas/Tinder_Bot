import pyautogui
import time
import threading

def autolike():
    print("Procurando a janela do BlueStacks App Player1...")
    time.sleep(1)
    
    windows = pyautogui.getWindowsWithTitle("BlueStacks App Player1")
    
    if len(windows) == 0:
        print("Janela do BlueStacks App Player1 não encontrada.")
        return
    elif len(windows) > 1:
        print("Mais de uma janela do BlueStacks App Player1 encontrada. Ativando a primeira.")
    
    # Ativando a primeira janela encontrada
    windows[0].activate()
    time.sleep(1)  # Dando um tempo para a janela ser ativada
    
    print("Iniciando autolike no Tinder...")
    
    # Supondo que você saiba a posição onde clicar para dar um "like"
    x, y = 200, 200  # Substitua esses valores pela posição que você marcou
    
    for i in range(10):  # Clica 10 vezes (você pode mudar este número)
        pyautogui.click(x, y)
        time.sleep(1)  # Espera 1 segundo entre os cliques

def show_position():
    while True:
        x, y = pyautogui.position()
        print(f'A posição atual do mouse é ({x}, {y})')
        time.sleep(1)

# Exibe a posição atual do mouse
show_position_thread = threading.Thread(target=show_position)
show_position_thread.daemon = True
show_position_thread.start()

# Chama a função para iniciar as curtidas
autolike()
