# print("Hello World")
# help(print)

# Moduly i przestzenie nazw
import os
import time
import czas
import importlib as imp

# current_path=os.getcwd() 
# print(current_path) 
aktualny_czas=czas.aktulany_czas
print(aktualny_czas)
time.sleep(20)
aktualny_czas=czas.aktulany_czas
print(aktualny_czas)
imp.reload(czas)
aktualny_czas=czas.aktulany_czas
print(aktualny_czas)

