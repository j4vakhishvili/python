from tkinter import *
X1 = 0
Y1 = 0
X2 = 1000
Y2 = 500
HEI = 500
WID = 1000
score1 = 0
score2 = 0
x = 4
y = 3 
counter = 0
yl0 = 0
stop = False
gamestart = False
yr0 = 0
speed = 3
root = Tk()
canvas = Canvas(root, width=WID, height=HEI, bg="#da58ff")

canvas.create_rectangle(X1, Y1, X2, Y2, fill="#40FF00")
canvas.create_rectangle(WID/2-2, Y1, WID/2+2, Y2, fill="white", outline="white")
canvas.create_oval(WID/2-30, Y2/2-30, WID/2+30, Y2/2+30, fill="white", outline="white")
left = canvas.create_rectangle(0, 0, 10, 100, fill="#0900FF")
right = canvas.create_rectangle(X2-10, 0, X2, 100, fill="#0900FF")
canvas.create_line(X1+10, Y1+10, X1+10, Y2, fill="white")
canvas.create_line(X2-10, 0, X2-10, Y2, fill="white")
ball = canvas.create_oval(WID/2-30, Y2/2-30, WID/2+30, Y2/2+30, fill="#380B61", outline="#380B61")
playerscore1 = canvas.create_text(X1+30, Y1+20, text=score1, font="Arial 20", fill="#0077FF")
playerscore2 = canvas.create_text(X2-30, Y1+20, text=score2, font="Arial 20", fill="#0077FF")
def move_ball():
    global x, y, yl0, yr0, ball, stop
    p = canvas.coords(ball)
    l = canvas.coords(left)
    r = canvas.coords(right)
    if p[0] <= l[2] and (l[1] < p[1] < l[3] or l[1] < p[3] < l[3]):
        if p[0] > -3:
            if 0 < x < 11:
                x = -(x+0.5)
            elif -11 < x < 0:
                x = -(x-0.5)
            else:
                x = -x
    if p[2] >= r[0] and (r[1] < p[1] < r[3] or r[1] < p[3] < r[3]):
        if p[2] < WID+3:
            if 0 < x < 11:
                x = -(x+0.5)
            elif -11 < x < 0:
                x = -(x-0.5)
            else:
                x = -x
    if p[1] <= -6 or p[3] >= HEI+6:
        y = -y
    score_checker(p[0], p[2])
    if p[0] < 0 or p[2] > WID:
        canvas.coords(ball, WID/2-30, Y2/2-30, WID/2+30, Y2/2+30)
        if x > 0:
            x = 5
        else:
            x = -5
    canvas.move(ball, x, y)
    canvas.move(left, 0, yl0)
    canvas.move(right, 0, yr0)
    if stop == True:
        pass
    elif stop == False:
        root.after(20, move_ball)
def move_pad(e):
    global yl0, yr0
    p = canvas.coords(left)
    l = canvas.coords(right)
    if e.keysym == "w":
        if p[3] >= 110:
            yl0 = -speed
        else:
            yl0 = 0

    if e.keysym == "s":
        if p[3] <= 500:
            yl0 = speed
        else:
            yl0 = 0

    if e.keysym == "Down":
        if l[3] <= 500:
            yr0 = speed
        else:
            yr0 = 0

    if e.keysym == "Up":
        if l[3] >= 110:
            yr0 = -speed
        else:
            yr0 = 0

def move_0(e):
    global yr0, yl0
    if e.keysym == "w" or e.keysym == "s":
        yl0 = 0
    if e.keysym == "Down" or e.keysym == "Up":
        yr0 = 0
def score_checker(x1, x2):
    global score1, score2, playerscore1, playerscore2
    if x1 < 0:
        score1 += 1
        canvas.itemconfig(playerscore2, text=score1)
    if x2 > WID:
        score2 += 1
        canvas.itemconfig(playerscore1, text=score2)

def sto():
    global stop, counter, gamestart
    if counter % 2 == 0 and gamestart == True:
        stop = True
        counter += 1
    elif counter % 2 == 1 and gamestart == True:
        stop = False
        move_ball()
        counter += 1
def gamestar():
    global gamestart, score1, score2, x, y
    if gamestart != True:
        move_ball()
        gamestart = True
    else:
        canvas.coords(ball, WID/2-30, Y2/2-30, WID/2+30, Y2/2+30)
        score1 = 0
        score2 = 0
        x = 5
        y = 4
        canvas.itemconfig(playerscore2, text=score1)
        canvas.itemconfig(playerscore1, text=score2)
        gamestart = True
button = Button(root, text="თამაშის დაწყება | ახალი თამაში", command=gamestar)
button2 = Button(root, text="თამაშის შეჩერება | თამაშის გაგრძელება", command=sto)
button.grid()
button2.grid()
canvas.bind("<KeyPress>", move_pad)
canvas.bind("<KeyRelease>", move_0)
canvas.focus_set()
canvas.grid()
root.title('პინგ პონგი (ქართულად)')


root.mainloop()
