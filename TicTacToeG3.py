#Importing Modules or Library
from tkinter import Tk,ttk,Button,messagebox,simpledialog

ActivePlayer = 1
p1 = []
p2 = []
mov = 0

#to fill symbol in 3x3 empty square grid and disable the block
def SetLayout(id,player_symbol):
    if id==1:
        b1.config(text= player_symbol)
        b1.state(['disabled'])
    elif id==2:
        b2.config(text= player_symbol)
        b2.state(['disabled'])
    elif id==3:
        b3.config(text= player_symbol)
        b3.state(['disabled'])
    elif id==4:
        b4.config(text= player_symbol)
        b4.state(['disabled'])
    elif id==5:
        b5.config(text= player_symbol)
        b5.state(['disabled'])
    elif id==6:
        b6.config(text= player_symbol)
        b6.state(['disabled'])
    elif id==7:
        b7.config(text= player_symbol)
        b7.state(['disabled'])
    elif id==8:
        b8.config(text= player_symbol)
        b8.state(['disabled'])
    elif id==9:
        b9.config(text= player_symbol)
        b9.state(['disabled'])

#to check and display who is the winner
def CheckWinner():
    global mov,name1,name2
    winner = 0

    if(1 in p1) and (2 in p1) and (3 in p1):
        winner = 1
    if(1 in p2) and (2 in p2) and (3 in p2):
        winner = 2

    if(4 in p1) and (5 in p1) and (6 in p1):
        winner = 1
    if(4 in p2) and (5 in p2) and (6 in p2):
        winner = 2

    if(7 in p1) and (8 in p1) and (9 in p1):
        winner = 1
    if(7 in p2) and (8 in p2) and (9 in p2):
        winner = 2

    if(1 in p1) and (4 in p1) and (7 in p1):
        winner = 1
    if(1 in p2) and (4 in p2) and (7 in p2):
        winner = 2

    if(2 in p1) and (5 in p1) and (8 in p1):
        winner = 1
    if(2 in p2) and (5 in p2) and (8 in p2):
        winner = 2

    if(3 in p1) and (6 in p1) and (9 in p1):
        winner = 1
    if(3 in p2) and (6 in p2) and (9 in p2):
        winner = 2

    if(1 in p1) and (5 in p1) and (9 in p1):
        winner = 1
    if(1 in p2) and (5 in p2) and (9 in p2):
        winner = 2

    if(3 in p1) and (5 in p1) and (7 in p1):
        winner = 1
    if(3 in p2) and (5 in p2) and (7 in p2):
        winner = 2

    if winner ==1:
        messagebox.showinfo(title="Congratulations.",
            message=(name1+" is the winner"))
    elif winner ==2:
        messagebox.showinfo(title="Congratulations.",
            message=(name2+" is the winner"))
    elif mov ==9:
        messagebox.showwarning(title="Draw", 
            message="   Match is DRAW!\nTRY USING TACTICS!!")

#where to place the symbol and to change title
def ButtonClick(id):
    global ActivePlayer,p1,p2,mov,name1,name2,pl1,pl2

    if ActivePlayer ==1:
        SetLayout(id,"X")
        p1.append(id)
        mov +=1
        root.title("Tic Tac Toe : "+name2)
        ActivePlayer =2
        root.configure(bg=pl2)

    elif ActivePlayer==2:
        SetLayout(id,"O")
        p2.append(id)
        mov +=1
        root.title("Tic Tac Toe : "+name1)
        ActivePlayer =1
        root.configure(bg=pl1)
    CheckWinner()

#enable all disabled block
def EnableAll():
    b1.config(text= " ")
    b1.state(['!disabled'])
    b2.config(text= " ")
    b2.state(['!disabled'])
    b3.config(text= " ")
    b3.state(['!disabled'])
    b4.config(text= " ")
    b4.state(['!disabled'])
    b5.config(text= " ")
    b5.state(['!disabled'])
    b6.config(text= " ")
    b6.state(['!disabled'])
    b7.config(text= " ")
    b7.state(['!disabled'])
    b8.config(text= " ")
    b8.state(['!disabled'])
    b9.config(text= " ")
    b9.state(['!disabled'])

#to restart the game
def Restart():
    global p1,p2,mov,ActivePlayer,name1,name2
    p1.clear(); p2.clear()
    mov,ActivePlayer = 0,1
    root.title("Tic Tac Toe : "+name1)
    root.configure(bg=pl1)
    EnableAll()

#Initializing main funtion
root = Tk()

name1=simpledialog.askstring("input","Name of PLAYER1?",parent=root)
name2=simpledialog.askstring("input","Name of PLAYER2?",parent=root)
pl1=simpledialog.askstring("input","what colour do you like {} ?".format(name1),parent=root)
pl2=simpledialog.askstring("input","what colour do you like {} ?".format(name2),parent=root)

root.title("Tic Tac toe :  "+name1)

#root.iconbitmap('C:/Users/HP/Downloads/python.ico')
root.geometry("900x530")
style = ttk.Style()
style.configure("my.TButton", font=('Roberto',24,'bold'))
root.configure(bg=pl1)

b1 = ttk.Button(root, text=" ", style="my.TButton")     #new style name.old style name
b1.grid(row=1, column=0,ipadx=50,ipady=50)
b1.config(command = lambda : ButtonClick(1)) 

b2 = ttk.Button(root, text=" ",style ="my.TButton")
b2.grid(row=1, column=1,ipadx=50, ipady=50)
b2.config(command = lambda : ButtonClick(2))

b3= ttk.Button(root, text=" ",style="my.TButton")
b3.grid(row=1, column=2,ipadx=50,ipady=50)
b3.config(command = lambda : ButtonClick(3))

b4 = ttk.Button(root, text=" ",style="my.TButton")
b4.grid(row=2, column=0,ipadx=50,ipady=50)
b4.config(command = lambda : ButtonClick(4))

b5 = ttk.Button(root, text=" ",style="my.TButton")
b5.grid(row=2, column=1,ipadx=50,ipady=50)
b5.config(command = lambda : ButtonClick(5))

b6 = ttk.Button(root, text=" ",style="my.TButton")
b6.grid(row=2, column=2,ipadx=50,ipady=50)
b6.config(command = lambda : ButtonClick(6))

b7 = ttk.Button(root, text=" ",style="my.TButton")
b7.grid(row=3, column=0,ipadx=50,ipady=50)
b7.config(command = lambda : ButtonClick(7))

b8 = ttk.Button(root, text=" ",style="my.TButton")
b8.grid(row=3, column=1,ipadx=50,ipady=50)
b8.config(command = lambda : ButtonClick(8))

b9 = ttk.Button(root, text=" ",style="my.TButton")
b9.grid(row=3, column=2,ipadx=50,ipady=50)
b9.config(command = lambda : ButtonClick(9))

Button(text="New Game", font=('Roberto', 22, 'bold'), bg='dark blue', fg='gold',
border=5, width=4,command = lambda :Restart()).grid(row=0, column=1,sticky="we")

root.resizable(0,0)
root.eval('tk::PlaceWindow . center')
root.mainloop()
