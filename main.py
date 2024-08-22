from tkinter import *

# Define grid coordinates
X = [[100, 250],[250, 400],[400, 550]]

a = []
b = []
t = 0  # Turn counter

# Boolean flags for each cell's availability
A = B = C = D = E = F = G = H = I = True

window = Tk()
c = 0
playerX_moves = set()  # Set to store X's moves
playerO_moves = set()  # Set to store O's moves

def checks(event):
    # Make global variables accessible
    global A, B, C, D, E, F, G, H, I
    
    # Check first column
    if event.x >= X[0][0] and event.x <= X[0][1]:
        if event.y >= X[0][0] and event.y <= X[0][1] and A:
            print("a")
            f = "a"
            where = [[X[0][0],X[0][0]],[X[0][1],X[0][1]]]
            draw(where,f)
            A = False
        if event.y >= X[1][0] and event.y <= X[1][1] and B:
            print("b")
            f = "b"
            where = [[X[0][0],X[1][0]],[X[0][1],X[1][1]]]
            draw(where,f)
            B = False
        if event.y >= X[2][0] and event.y <= X[2][1] and C:
            print("c")
            f = "c"
            where = [[X[0][0],X[2][0]],[X[0][1],X[2][1]]]
            draw(where,f)
            C = False
    
    # Check second column
    if event.x >= X[1][0] and event.x <= X[1][1]:
        if event.y >= X[1][0] and event.y <= X[1][1] and E:
            print("e")
            f = "e"
            where = [[X[1][0],X[1][0]],[X[1][1],X[1][1]]]
            draw(where,f)
            E = False
        if event.y >= X[2][0] and event.y <= X[2][1] and F:
            print("f")
            f = "f"
            where = [[X[1][0],X[2][0]],[X[1][1],X[2][1]]]
            draw(where,f)
            F = False
        if event.y >= X[0][0] and event.y <= X[0][1] and D:
            print("d")
            f = "d"
            where = [[X[1][0],X[0][0]],[X[1][1],X[0][1]]]
            draw(where,f)
            D = False
    
    # Check third column
    if event.x >= X[2][0] and event.x <= X[2][1]:
        if event.y >= X[2][0] and event.y <= X[2][1] and I:
            print("i")
            f = "i"
            where = [[X[2][0],X[2][0]],[X[2][1],X[2][1]]]
            draw(where,f)
            I = False
        if event.y >= X[1][0] and event.y <= X[1][1] and H:
            print("h")
            f = "h"
            where = [[X[2][0],X[1][0]],[X[2][1],X[1][1]]]
            draw(where,f)
            H = False
        if event.y >= X[0][0] and event.y <= X[0][1] and G:
            print("g")
            f = "g"
            where = [[X[2][0],X[0][0]],[X[2][1],X[0][1]]]
            draw(where,f)
            G = False
    Checker()

def draw(where, f):
    global t
    t += 1
    if t % 2 == 0:
        playerX_moves.add(f)  # Add move to X's set
        drawX(where)
    else:
        playerO_moves.add(f)  # Add move to O's set
        drawO(where)

def drawO(where):
    canvas.create_oval(where, width="10")

def drawX(where):
    canvas.create_line(where, width="10")
    canvas.create_line(where[0][0], where[1][1], where[1][0], where[0][1], width="10")

def Checker():
    # Define winning combinations
    winning_combinations = [
        {"a", "b", "c"}, {"d", "e", "f"}, {"g", "h", "i"},  # rows
        {"a", "d", "g"}, {"b", "e", "h"}, {"c", "f", "i"},  # columns
        {"a", "e", "i"}, {"c", "e", "g"}                    # diagonals
    ]
    
    # Check if either player has won
    for combo in winning_combinations:
        if combo.issubset(playerX_moves):
            print("X Winnsss!!!")
            A = B = C = D = E = F = G = H = I = False
            return
        if combo.issubset(playerO_moves):
            print("O Winnsss!!!")
            A = B = C = D = E = F = G = H = I = False
            return

# Create and set up the canvas
canvas = Canvas(window, width=600, height=600)
canvas.create_line(250, 100, 250, 550, width=5)
canvas.create_line(100, 250, 550, 250, width=5)
canvas.create_line(100, 400, 550, 400, width=5)
canvas.create_line(400, 100, 400, 550, width=5)

# Bind left mouse click to the checks function
window.bind("<Button-1>", checks)

canvas.pack()
window.mainloop()