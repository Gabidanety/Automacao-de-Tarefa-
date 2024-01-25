import pyautogui
import time 


pyautogui.PAUSE=3.0

#abrindo o navegador
pyautogui.press("win")
pyautogui.write("chorme")

time.sleep(3)
pyautogui.press("enter")

time.sleep(15)
pyautogui.click(x=455, y=904)

#abrindo site e fazendo login
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
time.sleep(5)
pyautogui.write(site)
pyautogui.press("enter")

time.sleep(7)
pyautogui.click(x=920, y=543)
pyautogui.write("GabiPy@gmail.com")
pyautogui.press("tab")
pyautogui.write("12345678")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

#cadastro dos produtos
import pandas as pd

tabela = pd.read_csv("produtos.csv") #pegando a tabela

for linha in tabela.index:
    pyautogui.click(x=1043, y=380)

    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")

    if not pd.isna (tabela.loc[linha,"obs"]): #se não estiver vazio ele cadastra
        pyautogui.write(str(tabela.loc[linha,"obs"]))
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)

#print(tabela)

