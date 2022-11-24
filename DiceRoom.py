import random
from tkinter import *

class Application(Frame):
    def __init__(self, master):
    #GUI------------------------------
        self.background = PhotoImage(file="C:\cosas\Downloads\pildoras\phyton\ejercicios\isaac\Dice Room\Dice_room.png")
        self.canvas1= Canvas(master, height=870, width=550)
        self.canvas1.pack(fill= BOTH, expand=True)
        self.canvas1.create_image(0, 0, image=self.background, anchor= NW)

        self.titulo= Label(self.canvas1, text="Clickea para tirar el dado:", bg="#4F0409")

        self.botonImage= PhotoImage(file="C:\cosas\Downloads\pildoras\phyton\ejercicios\isaac\Dice Room\Dice0.png")
        self.botonRollDado= Button(self.canvas1, 
                                image=self.botonImage,
                                command=lambda: self.tirarDados(), 
                                bg="#4F0409", 
                                borderwidth=0, 
                                highlightthickness = 0, 
                                bd = 0, 
                                highlightbackground="#600C16")

        self.labelDado= Label(self.canvas1, text="", bg="#4F0409", wraplength= 180)

        self.canvas_titulo = self.canvas1.create_window(425, 430, anchor=CENTER, window=self.titulo)
        self.canvas_boton_Dado = self.canvas1.create_window(425, 269, anchor=CENTER,window=self.botonRollDado)
        self.canvas_Dado = self.canvas1.create_window(575, 175, anchor=NW,window=self.labelDado)

    
#Metodos------------------------
    def tirarDados(self):
        roll = random.randint(1, 6)
        if roll == 1:
            self.imagenDado=PhotoImage(file="C:\cosas\Downloads\pildoras\phyton\ejercicios\isaac\Dice Room\Dice1.png")
            self.botonRollDado.config(image=self.imagenDado)
            self.botonRollDado.image = self.imagenDado
            self.labelDado.config(text="1 pip - Rerolls Isaac's currently held collectibles into items from the Treasure Room item pool, like the D4 would. Activated collectibles can be changed into passive ones, but passive collectibles cannot turn into activated ones.")
        elif roll == 2:
            self.imagenDado=PhotoImage(file="C:\cosas\Downloads\pildoras\phyton\ejercicios\isaac\Dice Room\Dice2.png")
            self.botonRollDado.config(image=self.imagenDado)
            self.botonRollDado.image = self.imagenDado
            self.labelDado.config(text="2 pips - Rerolls all pickups in the room, like the D20 would.")
        elif roll == 3:
            self.imagenDado=PhotoImage(file="C:\cosas\Downloads\pildoras\phyton\ejercicios\isaac\Dice Room\Dice3.png")
            self.botonRollDado.config(image=self.imagenDado)
            self.botonRollDado.image = self.imagenDado
            self.labelDado.config(text="3 pips - Rerolls all pickups and trinkets on the entire floor. This includes shop pickups. Does not reroll pickups or trinkets in the Devil Room, Angel Room, Black Market, or Crawl Space.")
        elif roll == 4:
            self.imagenDado=PhotoImage(file="C:\cosas\Downloads\pildoras\phyton\ejercicios\isaac\Dice Room\Dice4.png")
            self.botonRollDado.config(image=self.imagenDado)
            self.botonRollDado.image = self.imagenDado
            self.labelDado.config(text="4 pips - Rerolls any item pedestals on the floor, like The D6 would. Does not reroll item pedestals in the Devil Room, Angel Room, Library, Black Market, or Crawl Space.")
        elif roll == 5:
            self.imagenDado=PhotoImage(file="C:\cosas\Downloads\pildoras\phyton\ejercicios\isaac\Dice Room\Dice5.png")
            self.botonRollDado.config(image=self.imagenDado)
            self.botonRollDado.image = self.imagenDado
            self.labelDado.config(text="5 pips - Rerolls and restarts the current floor, which is the same effect as Forget Me Now.")
        else:
            self.imagenDado=PhotoImage(file="C:\cosas\Downloads\pildoras\phyton\ejercicios\isaac\Dice Room\Dice6.png")
            self.botonRollDado.config(image=self.imagenDado)
            self.botonRollDado.image = self.imagenDado
            self.labelDado.config(text="6 pips - Combines the effects of the 1-, 3-, and 4-pip rooms. (Rerolls all held items (including active), pickups, trinkets, and pedestal items like the D100.)")

#Main-------------------
master = Tk()
master.resizable(0,0)
master.title("Dice Room")
master.iconbitmap('C:\cosas\Downloads\pildoras\phyton\ejercicios\isaac\Dice Room\Dice_Room.ico')
master.geometry("870x540")

app = Application(master)

master.mainloop()