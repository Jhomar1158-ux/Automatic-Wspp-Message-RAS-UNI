#!pip install PyAutoGui
import pyautogui as pg
import webbrowser as web
import time
import pandas as pd

#data_dict = data.to_dict('list')
#celulares = data_dict['Telefono']
#nombres=data_dict['Nombre']
celular = '51_959254626'
nombre = 'Sandro'
combo=zip(nombres,celulares)
# 51_918009687

first = True
for nombre,celular in combo:
    time.sleep(8)
    mensaje=f"Hola {nombre} "
    web.open("https://web.whatsapp.com/send?phone="+celular+"&text="+mensaje)
    if first:
        time.sleep(8)
        first=False
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(10)
    pg.press('enter')
    time.sleep(6)
    pg.hotkey('ctrl', 'w')

first = True
time.sleep(8)
mensaje='Hola'
web.open("https://web.whatsapp.com/send?phone="+celular+"&text="+mensaje)
if first:
    time.sleep(8)
    first=False
width,height = pg.size()
pg.click(width/2,height/2)
time.sleep(8)
pg.press('enter')
time.sleep(1)
pg.hotkey('ctrl', 'w')