
from tkinter import BOTH


is_male = False
is_tall= True
if is_male and is_tall:                      #or= staci aby jedno z nich bylo pravdivy/ and= obe dve musi byt pravda
    print("You are a tall male")
elif is_male and not(is_tall):
    print("you are short male")
elif not(is_male) and is_tall:      #elif znamena else if pokud je ...  not udelas kdyz potrebujes vyresit False funkci je to false 
    print("You are not a male but you are tall")        
else:
    print("You are not a male and small")
    
    