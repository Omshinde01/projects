import random 
from random import randint
import colorama
from colorama import init,Fore,Back

i= 0
while True:
    colorama.init(autoreset=bool)

    comp= random.randint(1,3)
    comp=str(comp)
    if "1" in comp:
        choice= "r"
    elif "2" in comp:
        choice="p"
    elif "3" in comp:
        choice="s"
    print("computer have choosed!!")
    
    player= input("rock(r),paper(p) or scissors(s)...??? ")
    player.lower()
    if player == choice:
        a="draw"
    elif player =="p" and choice =="r":
        a=True
    elif player=="r" and choice=="s":
        a=True
    elif player=="s" and choice=="p":
        a=True
    elif player=="":
        print("no input from player!!!")
    else:
        a=False

    if a==True:
        print( (Fore.GREEN + "you won!!"))
    elif a==False:
        print(Fore.RED +"you lose!!")
    elif a=="draw":
        print(Fore.BLUE + "Game draw!!")
    

    print(f"computer choosed {choice}")
    print(f"you choosed {player}")


    print(Fore.YELLOW + "***********************NEW GAME*****************************")




