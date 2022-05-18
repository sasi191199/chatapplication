import pyautogui as pg
import time
time.sleep(10)
txt=open(r"C:\Users\HP\Downloads\animals.txt")
a = "Tharani is a"
for i in txt:
    pg.write(a+" "+i)
    pg.press("enter")
    