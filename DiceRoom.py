import random
from tkinter import *

root = Tk()
root.resizable(0,0)
root.title("Dice Room")
root.iconbitmap('C:\cosas\Downloads\pildoras\phyton\ejercicios\Dice Room\Dice_Room.ico')
root.geometry("870x540")

#Funciones------------------------
def tirarDados():
    roll = random.randint(1, 6)
    if roll == 1:
        imagenDado=PhotoImage(file="C:\cosas\Downloads\pildoras\phyton\ejercicios\Dice Room\Dice1.png")
        botonRollDado.config(image=imagenDado)
        botonRollDado.image = imagenDado
        labelDado.config(text="1 pip - Rerolls Isaac's currently held collectibles into items from the Treasure Room item pool, like the D4 would. Activated collectibles can be changed into passive ones, but passive collectibles cannot turn into activated ones.")
    elif roll == 2:
        imagenDado=PhotoImage(file="C:\cosas\Downloads\pildoras\phyton\ejercicios\Dice Room\Dice2.png")
        botonRollDado.config(image=imagenDado)
        botonRollDado.image = imagenDado
        labelDado.config(text="2 pips - Rerolls all pickups in the room, like the D20 would.")
    elif roll == 3:
        imagenDado=PhotoImage(file="C:\cosas\Downloads\pildoras\phyton\ejercicios\Dice Room\Dice3.png")
        botonRollDado.config(image=imagenDado)
        botonRollDado.image = imagenDado
        labelDado.config(text="3 pips - Rerolls all pickups and trinkets on the entire floor. This includes shop pickups. Does not reroll pickups or trinkets in the Devil Room, Angel Room, Black Market, or Crawl Space.")
    elif roll == 4:
        imagenDado=PhotoImage(file="C:\cosas\Downloads\pildoras\phyton\ejercicios\Dice Room\Dice4.png")
        botonRollDado.config(image=imagenDado)
        botonRollDado.image = imagenDado
        labelDado.config(text="4 pips - Rerolls any item pedestals on the floor, like The D6 would. Does not reroll item pedestals in the Devil Room, Angel Room, Library, Black Market, or Crawl Space.")
    elif roll == 5:
        imagenDado=PhotoImage(file="C:\cosas\Downloads\pildoras\phyton\ejercicios\Dice Room\Dice5.png")
        botonRollDado.config(image=imagenDado)
        botonRollDado.image = imagenDado
        labelDado.config(text="5 pips - Rerolls and restarts the current floor, which is the same effect as Forget Me Now.")
    else:
        imagenDado=PhotoImage(file="C:\cosas\Downloads\pildoras\phyton\ejercicios\Dice Room\Dice6.png")
        botonRollDado.config(image=imagenDado)
        botonRollDado.image = imagenDado
        labelDado.config(text="6 pips - Combines the effects of the 1-, 3-, and 4-pip rooms. (Rerolls all held items (including active), pickups, trinkets, and pedestal items like the D100.)")

#GUI------------------------------
background = PhotoImage(file="C:\cosas\Downloads\pildoras\phyton\ejercicios\Dice Room\Dice_room.png")
canvas1= Canvas(root, height=870, width=550)
canvas1.pack(fill= BOTH, expand=True)
canvas1.create_image(0, 0, image=background, anchor= NW)

titulo= Label(canvas1, text="Clickea para tirar el dado:", bg="#4F0409")

botonImage= PhotoImage(file="C:\cosas\Downloads\pildoras\phyton\ejercicios\Dice Room\Dice0.png")
botonRollDado= Button(canvas1, 
                        image=botonImage,
                        command=tirarDados, 
                        bg="#4F0409", 
                        borderwidth=0, 
                        highlightthickness = 0, 
                        bd = 0, 
                        highlightbackground="#600C16")

labelDado= Label(canvas1, text="", bg="#4F0409", wraplength= 180)

canvas_titulo = canvas1.create_window(425, 430, anchor=CENTER, window=titulo)
canvas_boton_Dado = canvas1.create_window(425, 269, anchor=CENTER,window=botonRollDado)
canvas_Dado = canvas1.create_window(575, 175, anchor=NW,window=labelDado)

root.mainloop()