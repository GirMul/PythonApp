import tkinter as tk
import time
import sys

print("Starting BallGame container...", flush=True)

# Game constants
WIDTH = 600
HEIGHT = 400

root = tk.Tk()
root.title("Ball Game (Docker Mode)")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

ball = canvas.create_oval(290, 190, 310, 210, fill="red")

dx = 3
dy = 3

def move_ball():
    global dx, dy
    canvas.move(ball, dx, dy)
    x1, y1, x2, y2 = canvas.coords(ball)

    if x1 <= 0 or x2 >= WIDTH:
        dx = -dx
        print("Ball hit vertical wall", flush=True)

    if y1 <= 0 or y2 >= HEIGHT:
        dy = -dy
        print("Ball hit horizontal wall", flush=True)

    root.after(100, move_ball)

print("BallGame initialized successfully", flush=True)

move_ball()
root.mainloop()
