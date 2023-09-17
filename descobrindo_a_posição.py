import pyautogui
import time
import tkinter as tk
from tkinter import messagebox
import threading

def autolike():
    print("Iniciando autolike no Tinder...")
    time.sleep(2)
    
    # Supondo que você saiba a posição onde clicar para dar um "like"
    x, y = pyautogui.position()
    
    for i in range(10):  # Clica 10 vezes (você pode mudar este número)
        pyautogui.click(x, y)
        time.sleep(1)  # Espera 1 segundo entre os cliques

def show_position():
    while True:
        x, y = pyautogui.position()
        print(f'A posição atual do mouse é ({x}, {y})')
        time.sleep(1)

def prompt():
    answer = messagebox.askyesno("Confirmação", "Podemos começar as curtidas no Tinder?")
    if answer:
        autolike()
    else:
        print("Operação cancelada.")

# Cria uma janela de aplicação Tkinter
root = tk.Tk()
root.withdraw()  # Esconde a janela principal

# Exibe a posição atual do mouse
show_position_thread = threading.Thread(target=show_position)
show_position_thread.daemon = True
show_position_thread.start()

# Exibe a caixa de diálogo
prompt()
