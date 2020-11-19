from tkinter import *
import random
width=600
height=600
seg_size=30
root=Tk()

frame=Frame(root,height='30',width='600')
frame.pack()
c=Canvas(root,height=height,width=width,bg="black")
fps=120
c.pack()

count=0
in_game = True
paused = True
def pause():
    global paused
    
    if(paused):
        pause_btn.config(text="გაგრძელება")
        paused = False
    else:
        pause_btn.config(text="შეჩერება")
        paused = True

    
label = Label(frame,text="ქულები: {}".format(count),font="Arial 18")
label.pack(side=RIGHT)
pause_btn = Button(frame,text="შეჩერება",command=pause)

pause_btn.pack(side=LEFT)


class Segment:
    def __init__(self,x,y):
        list_colors=["green"]
        if(count==0):
            self.segment = c.create_rectangle(x,y,x+seg_size,y+seg_size,fill="#A0FF77")
        else:
            self.segment = c.create_rectangle(x,y,x+seg_size,y+seg_size,fill=random.choice(list_colors))

class Snake:
    def __init__(self,segments):
        
        self.segments = segments
        self.mapping={"Up":(0,-1),"Down":(0,1),"Right":(1,0),"Left":(-1,0)}
        self.vector=self.mapping["Right"]
        self.move()
        
        
        
    def move(self):
        global in_game
        if(paused):
            c.focus_set()
        else:
            pause_btn.focus_set()
        
        if (in_game and paused):
            for index in range(len(self.segments)-1):
                segment=self.segments[index].segment
                c.coords(segment,c.coords(self.segments[index+1].segment))
            x1,y1,x2,y2 = c.coords(self.segments[-1].segment)
            c.coords(self.segments[-1].segment,
                     x1+self.vector[0]*seg_size,y1+self.vector[1]*seg_size,
                     x2+self.vector[0]*seg_size,y2+self.vector[1]*seg_size)
            self.head_coords = c.coords(self.segments[-1].segment)
            
        self.grow()
        self.game_over()
        root.after(100,self.move)
        
    def change_direction(self,event):
        vert = ("Up","Down")
        horiz = ("Right","Left")
        back = True
        if(event.keysym == vert[0] and self.vector == self.mapping[vert[1]]):
            back=False
        elif(event.keysym == vert[1] and self.vector==self.mapping[vert[0]]):
            back=False
        elif(event.keysym == horiz[0] and self.vector==self.mapping[horiz[1]]):
            back = False
        elif(event.keysym == horiz[1] and self.vector==self.mapping[horiz[0]]):
            back = False
        print(back)
        if (event.keysym in self.mapping):
            if(back):
                self.vector = self.mapping[event.keysym]
        if(event.keysym =='p'):
            pause()
        
    def grow(self):
        global a
        global count
        global label
        x1,y1,x2,y2 = c.coords(self.segments[0].segment)
        if(self.head_coords == a.apple_coords):
            a.del_apple()
            count+=1
            label.config(text="ქულები: {}".format(count))
            self.segments.insert(0,Segment(x2,y1))
            a = Apple()
    def game_over(self):
        global in_game
        if(self.head_coords[0]<-1 or self.head_coords[2]>width+1 or self.head_coords[1]<-1 or self.head_coords[3]>height+1):
            print(self.head_coords)
            in_game=False
            for i in  self.segments:
                del i
            a.del_apple()
            self.text1=c.create_text(width/10+230,height/7+80,text="By Nikoloz Javakhishvili",font="Arial 10",fill="Green")
            self.text1=c.create_text(width/2,height/2,text="თამაში დასრულდა",font="Arial 30",fill="#00D0C2")
            self.text2=c.create_text(width/2,height/2+40,text="აგროვებულია {} ქულა, არაუშავს შემდეგში გაგიმართლებს =)".format(count),font="Arial 14",fill="#007A72")
class Apple:
    def __init__(self):
        x=random.randint(0,19)
        y=random.randint(0,19)
        self.oval=c.create_rectangle(x*seg_size,y*seg_size,x*seg_size+seg_size,y*seg_size+seg_size,fill="#FCFF00")
        self.apple_coords=c.coords(self.oval)
    def del_apple(self):
        c.delete(self.oval)
    
segments=[Segment(seg_size,seg_size)]     
a=Apple()
def main():
    
    s =  Snake(segments)
    c.bind("<Key>",s.change_direction)

root.title("Snake [ By Nikoloz Javakhishvili ]")    
main()
root.mainloop()       