## ______________________________  ____  ________
## \_   _____/\_   _____/\_____  \/_   |/  _____/
##  |    __)   |    __)_   _(__  < |   /   __  \ 
##  |     \    |        \ /       \|   \  |__\  \
##  \___  /   /_______  //______  /|___|\_____  /
##      \/            \/        \/            \/ 
## Shout_out_matrix v0.1

from time import sleep
from os import system
   
if __name__=="__main__":
# PRINT CICLE
    def ciclo(lista):
        output=""
        i=0
        for i in range (len(lista)):
            a=lista[i]
            output=output+a
            sleep (0.1)
            system("clear")
            print(output)
# START 
    system("clear")
    sleep(3)
    with open ("text_matrix.txt","r") as ft:
        while True:
            line=ft.readline()
            lista=list(line)
            if lista[0] != ";":
                ciclo(lista)
                sleep(3)
            else:
                break
# MATRIX
sleep (4)
system("unimatrix -f -b -l k -s 95 -t 8")
system("clear")
print("Shout_out_matrix")
print("Coded by: Fe316 - 2021")
sleep(20)
# end
