import time
import pyautogui
import pyperclip

time.sleep(3)  # tempo pra clicar no Mocha

# navegação/login de exemplo
pyautogui.press("f3")
time.sleep(0.2)
pyautogui.typewrite("wssn")
pyautogui.press("enter")
time.sleep(0.2)
pyautogui.typewrite("902")
pyautogui.press("tab")
pyautogui.typewrite("516421838") 
pyautogui.press("tab")
pyautogui.typewrite("Fresno#32")
pyautogui.press("enter")
time.sleep(0.2)
pyautogui.click(200, 200)

# Espera carregar a tela
time.sleep(1)

# Copia a tela
pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "c")
texto = pyperclip.paste()

print("Tela Capturada:")
print(texto)
