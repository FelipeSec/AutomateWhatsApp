import webbrowser
import time
import pyautogui as gui 

cell_numbers ={
    //insira os números
}

interval = 2
position = 677, 372
numbers= cell_numbers

message = input('Insira a Mensagem:')

for i in numbers:
 url = 'https://wa.me/{}?text={}'.format(i, message)
 webbrowser.open(url)
 time.sleep(3)
 gui.click(position)
 time.sleep(3)
 gui.press('enter')
 time.sleep(interval)
