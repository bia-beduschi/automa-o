# Passo a passo do Projeto
# Bibliotecas
import pyautogui
import time
import pandas  # pip install pandas numby openpyxl

# Passo 1: Entrar no sistema da empresa 
    # Site: https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Para instalar: pip install pandas pyautogui
# pyautogui.click -> clicar com mouse 
# pyautogui.write -> escreva um texto
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> atalho (combinação de teclas)

pyautogui.PAUSE = 1 # Todos pyautogui vao ter um tempo de 0.4 para serem executados

# abrir o chrome 
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1) # tempo apenas para essa operacao
pyautogui.click(x=685, y=436) 

# entrar no link 
time.sleep(0.5) # tempo apenas para essa operacao
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# esperar o site carregar
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=640, y=401)
pyautogui.write("beatrizbeduchitaiao@gmail.com")
pyautogui.press("tab")
pyautogui.write("automacaopython")
pyautogui.press("enter")
time.sleep(1)

# Passo 3: Importar a base de dados de produtos 
tabela = pandas.read_csv("produtos.csv")
print(tabela)

 # Passo 4: cadastrar um produto # Passo e repetir o cadastro para todos os produtos 
for linha in tabela.index:
    pyautogui.click(x=596, y=283)
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]

    # Preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # se estiver vazio, nao executar
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    # apertar para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
