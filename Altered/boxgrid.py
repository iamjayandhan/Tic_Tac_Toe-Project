from tkinter import Tk, ttk, Button, messagebox, simpledialog

ActivePlayer = 1
p1 = []
p2 = []
mov = 0
board_size = 3
buttons = {}

# Function to fill symbol in the grid and disable the block
def SetLayout(id, player_symbol):
    buttons[id].config(text=player_symbol)
    buttons[id].state(['disabled'])

# Function to check and display the winner
def CheckWinner():
    global mov, name1, name2
    winner = 0
    

    # Rows
    for i in range(board_size):
        if all(x in p1 for x in range(i * board_size + 1, (i + 1) * board_size + 1)):
            winner = 1
        if all(x in p2 for x in range(i * board_size + 1, (i + 1) * board_size + 1)):
            winner = 2

    # Columns
    for i in range(board_size):
        if all(x in p1 for x in range(i + 1, board_size ** 2 + 1, board_size)):
            winner = 1
        if all(x in p2 for x in range(i + 1, board_size ** 2 + 1, board_size)):
            winner = 2

    # Diagonal (top-left to bottom-right)
    if all(x in p1 for x in range(1, board_size ** 2 + 1, board_size + 1)):
        winner = 1
    if all(x in p2 for x in range(1, board_size ** 2 + 1, board_size + 1)):
        winner = 2

    # Diagonal (top-right to bottom-left)
    if all(x in p1 for x in range(board_size, board_size ** 2 - board_size + 1, board_size - 1)):
        winner = 1
    if all(x in p2 for x in range(board_size, board_size ** 2 - board_size + 1, board_size - 1)):
        winner = 2

    if winner == 1:
        messagebox.showinfo(title="Congratulations.", message=(name1 + " is the winner"))
    elif winner == 2:
        messagebox.showinfo(title="Congratulations.", message=(name2 + " is the winner"))
    elif mov == board_size ** 2:
        messagebox.showwarning(title="Draw", message="Match is DRAW!\nTRY USING TACTICS!!")

# Function to handle button click
# Function to handle button click
def ButtonClick(id):
    global ActivePlayer, p1, p2, mov, name1, name2

    if ActivePlayer == 1:
        SetLayout(id, "X")
        p1.append(id)
        mov += 1
        root.title("Tic Tac Toe : " + name2)
        root.configure(bg=pl2)
        ActivePlayer = 2
    elif ActivePlayer == 2:
        SetLayout(id, "O")
        p2.append(id)
        mov += 1
        root.title("Tic Tac Toe : " + name1)
        root.configure(bg=pl1)
        ActivePlayer = 1

    buttons[id].state(['disabled'])
    CheckWinner()

# Function to enable all buttons
def EnableAll():
    for button in buttons.values():
        button.config(text=" ")
        button.state(['!disabled'])

# Function to restart the game
def Restart():
    global p1, p2, mov, ActivePlayer, name1, name2
    p1.clear()
    p2.clear()
    mov, ActivePlayer = 0, 1
    root.title("Tic Tac Toe : " + name1)
    root.configure(bg=pl1)
    EnableAll()

# Function to change the board size and restart the game
def ChangeBoardSize(size):
    global board_size
    board_size = size

    for button in buttons.values():
        button.destroy()

    CreateButtons()
    Restart()

# Function to create buttons based on the board size
def CreateButtons():
    global buttons, board_size

    buttons = {}

    for i in range(1, board_size**2 + 1):
        button = ttk.Button(root, style="my.TButton")
        button.grid(row=(i - 1) // board_size + 1, column=(i - 1) % board_size, ipadx=50, ipady=50)
        button.config(command=lambda id=i: ButtonClick(id))
        buttons[i] = button

# Initialize main function
root = Tk()

name1 = simpledialog.askstring("Input", "Name of PLAYER1?", parent=root)
name2 = simpledialog.askstring("Input", "Name of PLAYER2?", parent=root)
pl1 = simpledialog.askstring("Input", "What color do you like, {}?".format(name1), parent=root)
pl2 = simpledialog.askstring("Input", "What color do you like, {}?".format(name2), parent=root)

root.title("Tic Tac Toe : " + name1)

root.geometry("900x530")
style = ttk.Style()
style.configure("my.TButton", font=('Arial', 24, 'bold'))
root.configure(bg=pl1)

CreateButtons()

ttk.Button(text="New Game", style="my.TButton", command=lambda: Restart()).grid(row=0, column=1, sticky="we")

# Toggle window to change board size
toggle_window = ttk.Label(root, text="Board Size:", font=('Arial', 14, 'bold'), background='white', padding=(10, 5))
toggle_window.grid(row=0, column=2, sticky="e")
ttk.Button(toggle_window, text="3x3", command=lambda: ChangeBoardSize(3)).grid(row=0, column=0)
ttk.Button(toggle_window, text="4x4", command=lambda: ChangeBoardSize(4)).grid(row=0, column=1)
ttk.Button(toggle_window, text="5x5", command=lambda: ChangeBoardSize(5)).grid(row=0, column=2)

root.resizable(True, True)
root.eval('tk::PlaceWindow . center')
root.mainloop()
