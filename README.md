# Documentação para o script do Tinder Bot

Esse script foi desenvolvido para automatizar a ação de dar "likes" no aplicativo Tinder, que está rodando em uma máquina virtual no BlueStacks App Player 1. Para entender como ele funciona, vamos detalhar cada parte do código.

## Importação de Bibliotecas

```python
import pyautogui
import time
import threading
```

- `pyautogui`: Utilizado para automação da interface gráfica.
- `time`: Utilizado para criar atrasos entre ações.
- `threading`: Utilizado para executar várias funções simultaneamente.

## Função `autolike`

```python
def autolike():
    print("Procurando a janela do BlueStacks App Player1...")
    time.sleep(1)
    ...
```

Essa função é responsável por realizar os "likes" automaticamente.

### Encontrando e Ativando a Janela do BlueStacks

```python
windows = pyautogui.getWindowsWithTitle("BlueStacks App Player 1")
...
windows[0].activate()
```

O script procura pela janela do BlueStacks e, se encontrar, a ativa para que as ações futuras ocorram nessa janela.

### Realizando os "Likes"

```python
x, y = 1441, 847
...
pyautogui.click(x, y)
```

Aqui, o script executa 10 cliques nas coordenadas (1441, 847). Você deve substituir essas coordenadas pela posição do botão de "like" no seu setup.

## Função `show_position`

```python
def show_position():
    ...
```

Essa função é responsável por mostrar a posição atual do mouse. É útil para encontrar as coordenadas onde você deseja clicar.

## Multi-threading

```python
show_position_thread = threading.Thread(target=show_position)
show_position_thread.daemon = True
show_position_thread.start()
```

Essa parte do código cria um novo thread para a função `show_position`, permitindo que ela seja executada em paralelo com a função `autolike`.

## Executando o script

Por último, a função `autolike` é chamada para iniciar o processo.

```python
autolike()
```

Para executar o script, você deve ter o BlueStacks App Player 1 aberto e o Tinder rodando dentro dele. O script então ativará a janela e começará a dar "likes" automaticamente.