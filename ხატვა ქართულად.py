from tkinter import *


class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.color = "black"
        self.brush_size = 2
        self.setUI()

    def set_color(self, new_color):
        self.color = new_color

    def set_brush_size(self, new_size):
        self.brush_size = new_size

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)

    def setUI(self):

        self.parent.title("Smart Paint GE")
        self.pack(fill=BOTH, expand=1) 

        self.columnconfigure(6, weight=1) 
        self.rowconfigure(2, weight=1) 

        self.canv = Canvas(self, bg="white")  
        self.canv.grid(row=2, column=0, columnspan=8,
                       padx=5, pady=5, sticky=E+W+S+N) 
        self.canv.bind("<B1-Motion>", self.draw) 

        color_lab = Label(self, text="ფერი: ") 
        color_lab.grid(row=0, column=0, padx=6) 

        red_btn = Button(self, text="წითელი", width=10,
                         command=lambda: self.set_color("#FF0000"))
        red_btn.grid(row=0, column=1)
  
        green_btn = Button(self, text="მწვანე", width=10,
                           command=lambda: self.set_color("#55FF00"))
        green_btn.grid(row=0, column=2)

        blue_btn = Button(self, text="ლურჯი", width=10,
                          command=lambda: self.set_color("#1100FF"))
        blue_btn.grid(row=0, column=3)

        black_btn = Button(self, text="შავი", width=10,
                           command=lambda: self.set_color("black"))
        black_btn.grid(row=0, column=4)

        white_btn = Button(self, text="ყვითელი", width=10,
                           command=lambda: self.set_color("yellow"))
        white_btn.grid(row=0, column=5)
        
        white_btn = Button(self, text="ყავისფერი", width=12,
                           command=lambda: self.set_color("brown"))
        white_btn.grid(row=0, column=6)
        
        clear_btn = Button(self, text="ფონის გასუფთავება", width=17,
                           command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=7, sticky=W)

        size_lab = Label(self, text="ფანქრის ზომა: ")
        size_lab.grid(row=1, column=0, padx=5)
        one_btn = Button(self, text="ორი", width=10,
                         command=lambda: self.set_brush_size(2))
        one_btn.grid(row=1, column=1)

        two_btn = Button(self, text="ხუთი", width=10,
                         command=lambda: self.set_brush_size(5))
        two_btn.grid(row=1, column=2)

        five_btn = Button(self, text="შვიდი", width=10,
                          command=lambda: self.set_brush_size(7))
        five_btn.grid(row=1, column=3)

        seven_btn = Button(self, text="ათი", width=10,
                           command=lambda: self.set_brush_size(10))
        seven_btn.grid(row=1, column=4)

        ten_btn = Button(self, text="ოცი", width=10,
                         command=lambda: self.set_brush_size(20))
        ten_btn.grid(row=1, column=5)

        twenty_btn = Button(self, text="ორმოცდაათი", width=15,
                            command=lambda: self.set_brush_size(50))
        twenty_btn.grid(row=1, column=6, sticky=W)
        
        white_btn = Button(self, text="საშლელი", width=17,
                           command=lambda: self.set_color("white"))
        white_btn.grid(row=1, column=7)


def main():
    root = Tk()
    root.geometry("720x500+600+200")
    root.resizable(False, False)
    app = Paint(root)
    root.mainloop()

if __name__ == '__main__':
    main()