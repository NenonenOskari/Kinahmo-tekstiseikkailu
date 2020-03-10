import os
import sys
import time
from time import sleep

#koordinaatit:



def main_gameplay_loop():
    s = 'eiooexit'
    while s != 'exit':
        liikkuminen()
        print('sijainti: ')
        print(get_koordinaatit())
        kuvailu(x,y)
        sleep(3)
        toiminta(x,y)

def kuvailu(x,y):
    print('Tähän kuvaus paikasta')

def toiminta(x,y):
    print('tähän sitten oikean paikan keskustelujen yms. väkivallan hakeminen')
    
def ukki_lukee(nimi):
    path = os.path.join(sys.path[0])
    path += "/story/" + nimi
    tarina = open(path, "r", encoding='utf8')
    for x in tarina:
        print(x)
        sleep(0.1)
    tarina.close()

def liikkuminen():
    valinta = 1
    lx = get_x()
    ly = get_y()
    while valinta == 1:
        print("Valitse liikkumissuunta")
        print("Pohjoinen P\nEtelä E\nItä I\nLänsi L")
        suunta = input()
        if suunta == "Pohjoinen" or suunta == "P" or suunta == "p":
            print("Liikut pohjoiseen")
            set_koordinaatit(lx,ly+1)
            valinta = 2
        elif suunta == "Etelä" or suunta == "E" or suunta == "e":
            print("Liikut etelään")
            set_koordinaatit(lx,ly-1)
            valinta = 2
        elif suunta == "Itä" or suunta == "I" or suunta == "i":
            print("Liikut itään")
            set_koordinaatit(lx+1,ly)
            valinta = 2
        elif suunta == "Länsi" or suunta == "L" or suunta == "l":
            print("Liikut länsi")
            set_koordinaatit(lx-1,ly)
            valinta = 2
        else:
            print("Syötä suunta liikkuaksesi, P,E,I tai L")


def set_koordinaatit(xx,yy):
    global x
    x = xx
    global y
    y = yy

def get_x():
    return x
def get_y():
    return y
def get_koordinaatit():
    return([x,y])



#Asetetaan aloituskoordinaatit:
set_koordinaatit(5,5)
print('Aloituspositio: ')
print(get_koordinaatit())

#ukki_lukee("alku.txt")
main_gameplay_loop()
#ukki_lukee("merihirvi.txt")


