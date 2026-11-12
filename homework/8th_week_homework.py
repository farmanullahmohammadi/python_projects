
import tkinter as tk
import random

root = tk.Tk()
root.title("Mini Animation Game")
root.geometry("600x480")

canvas = tk.Canvas(root, width=550,
                   height=350, bg="white")
canvas.pack(pady=10)

player = canvas.create_rectangle(
    30, 150, 70, 190,
    fill="blue", tags="player"
)

ball = canvas.create_oval(
    200, 100, 240, 140,
    fill="red", tags="ball"
)

obstacle = canvas.create_rectangle(
    400, 100, 440, 160,
    fill="green", tags="obstacle"
)

score = 0
dx = 4
running = False
job = None

label = tk.Label(root, text="Score: 0")
label.pack()

def move_player(event):
    x1, y1, x2, y2 = canvas.coords(player)

    if event.keysym == "Left" and x1 > 0:
        canvas.move(player, -10, 0)

    elif event.keysym == "Right" and x2 < 550:
        canvas.move(player, 10, 0)

    elif event.keysym == "Up" and y1 > 0:
        canvas.move(player, 0, -10)

    elif event.keysym == "Down" and y2 < 350:
        canvas.move(player, 0, 10)

def animate():
    global dx, job

    if not running:
        return

    x1, y1, x2, y2 = canvas.coords(ball)

    if x1 <= 0 or x2 >= 550:
        dx = -dx

    canvas.move(ball, dx, 0)

    job = root.after(30, animate)

def start():
    global running

    if not running:
        running = True
        animate()

def pause():
    global running, job

    running = False

    if job is not None:
        root.after_cancel(job)
        job = None

def reset():
    global score, dx

    pause()

    canvas.coords(player, 30, 150, 70, 190)
    canvas.coords(ball, 200, 100, 240, 140)
    canvas.coords(obstacle, 400, 100, 440, 160)

    score = 0
    dx = 4
    label.config(text="Score: 0")

def click_ball(event):
    global score

    items = canvas.find_overlapping(
        event.x, event.y,
        event.x, event.y
    )

    if ball in items:
        score += 1
        label.config(text=f"Score: {score}")

        canvas.coords(
            ball,
            random.randint(50, 450),
            random.randint(50, 250),
            random.randint(90, 490),
            random.randint(90, 290)
        )

def drag(event):
    canvas.coords(
        obstacle,
        event.x-20, event.y-20,
        event.x+20, event.y+20
    )

canvas.bind("<Button-1>", click_ball)
canvas.tag_bind("obstacle", "<B1-Motion>", drag)

root.bind("<KeyPress>", move_player)

tk.Button(root, text="Start",
          command=start).pack(side="left", padx=20)

tk.Button(root, text="Pause",
          command=pause).pack(side="left")

tk.Button(root, text="Reset",
          command=reset).pack(side="left")

root.mainloop()
