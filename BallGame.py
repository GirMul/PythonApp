import tkinter as tk

# Window setup
WIDTH = 600
HEIGHT = 400

root = tk.Tk()
root.title("Small Ball Game")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Create ball
ball = canvas.create_oval(290, 190, 310, 210, fill="red")

# Ball movement
dx = 3
dy = 3

def move_ball():
    global dx, dy
    canvas.move(ball, dx, dy)

    x1, y1, x2, y2 = canvas.coords(ball)

    # Bounce off walls
    if x1 <= 0 or x2 >= WIDTH:
        dx = -dx
    if y1 <= 0 or y2 >= HEIGHT:
        dy = -dy

    root.after(20, move_ball)

# Keyboard controls
def move_left(event):
    canvas.move(ball, -20, 0)

def move_right(event):
    canvas.move(ball, 20, 0)

def move_up(event):
    canvas.move(ball, 0, -20)

def move_down(event):
    canvas.move(ball, 0, 20)

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)

# Start game
move_ball()
root.mainloop()
