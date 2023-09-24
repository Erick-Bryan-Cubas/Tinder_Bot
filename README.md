Tinder Bot com Python

Este repositório contém um script em Python para automatizar "likes" no Tinder. O código utiliza as bibliotecas `pyautogui`, `time`, `tkinter` e `threading`.

## Como funciona

### Importação de Módulos
```python
import pyautogui
import time
import tkinter as tk
from tkinter import messagebox
import threading
```
- `pyautogui`: Para simular cliques do mouse e interações com a interface do usuário.
- `time`: Para gerenciar o tempo entre os cliques.
- `tkinter` e `messagebox`: Para criar uma caixa de diálogo de confirmação.
- `threading`: Para executar tarefas em paralelo.

### Função `autolike`
```python
def autolike():
    print("Iniciando autolike no Tinder...")
    time.sleep(2)
    x, y = pyautogui.position()
    for i in range(10):
        pyautogui.click(x, y)
        time.sleep(1)
```
Esta função executa a automação dos "likes". Ela aguarda 2 segundos, obtém a posição atual do mouse e faz 10 cliques em intervalos de 1 segundo.

### Função `show_position`
```python
def show_position():
    while True:
        x, y = pyautogui.position()
        print(f'A posição atual do mouse é ({x}, {y})')
        time.sleep(1)
```
Esta função imprime a posição atual do mouse a cada segundo. Isso é útil para saber onde colocar o mouse antes de iniciar a automação.

### Função `prompt`
```python
def prompt():
    answer = messagebox.askyesno("Confirmação", "Podemos começar as curtidas no Tinder?")
    if answer:
        autolike()
    else:
        print("Operação cancelada.")
```
Exibe uma caixa de diálogo para confirmar se o usuário deseja começar a automação.

### Interface Gráfica e Threading
```python
root = tk.Tk()
root.withdraw()
show_position_thread = threading.Thread(target=show_position)
show_position_thread.daemon = True
show_position_thread.start()
prompt()
```
- Uma janela Tkinter é criada e imediatamente escondida.
- Um thread é criado para a função `show_position`, permitindo que ela execute em paralelo.
- A caixa de diálogo é exibida chamando a função `prompt()`.

## Uso
1. Certifique-se de instalar todas as bibliotecas necessárias.
2. Posicione o mouse onde o "like" deve ser clicado no Tinder.
3. Execute o script e confirme a ação na caixa de diálogo.

