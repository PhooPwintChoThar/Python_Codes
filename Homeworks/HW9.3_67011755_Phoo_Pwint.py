from tkinter import *

class Circle:
    def init(self):
        window=Tk()
        window.title("tk")
        self.canvas=Canvas(window)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Button-1>", self.clickLeft)
        self.canvas.bind("<Button-3>", self.clickRight)
        window.mainloop()

    def clickLeft(self,event):
        self.canvas.create_oval(event.x-30, event.y-30, event.x+30, event.y+30, tags="circle")
    def clickRight(self,event):
        items=self.canvas.find_overlapping(event.x-30, event.y-30, event.x+30, event.y+30)
        for x in items:
            tags=self.canvas.gettags(x)
            if "circle" in tags :
                self.canvas.delete(x)

Circle()
