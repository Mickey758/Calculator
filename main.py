from tkinter import *
from tkinter import Tk

class gui(Tk):
    def __init__(self):
        super().__init__()
        self.text = Text(width=13,height=1,font=("Space Mono",25));self.text.pack()
        
        col1 = Frame();col1.pack()
        Button(col1,text="1",width=8,height=3,command=lambda:self.add("1")).pack(side=LEFT)
        Button(col1,text="2",width=8,height=3,command=lambda:self.add("2")).pack(side=LEFT)
        Button(col1,text="3",width=8,height=3,command=lambda:self.add("3")).pack(side=LEFT)
        Button(col1,text="+",width=8,height=3,command=lambda:self.add("+")).pack(side=LEFT)
        
        col2 = Frame();col2.pack()
        Button(col2,text="4",width=8,height=3,command=lambda:self.add("4")).pack(side=LEFT)
        Button(col2,text="5",width=8,height=3,command=lambda:self.add("5")).pack(side=LEFT)
        Button(col2,text="6",width=8,height=3,command=lambda:self.add("6")).pack(side=LEFT)
        Button(col2,text="-",width=8,height=3,command=lambda:self.add("-")).pack(side=LEFT)
        
        col3 = Frame();col3.pack()
        Button(col3,text="7",width=8,height=3,command=lambda:self.add("7")).pack(side=LEFT)
        Button(col3,text="8",width=8,height=3,command=lambda:self.add("8")).pack(side=LEFT)
        Button(col3,text="9",width=8,height=3,command=lambda:self.add("9")).pack(side=LEFT)
        Button(col3,text="*",width=8,height=3,command=lambda:self.add("*")).pack(side=LEFT)
    
        col4 = Frame();col4.pack()
        Button(col4,text=".",width=8,height=3,command=lambda:self.add(".")).pack(side=LEFT)
        Button(col4,text="0",width=8,height=3,command=lambda:self.add("0")).pack(side=LEFT)
        Button(col4,text="/",width=8,height=3,command=lambda:self.add("/")).pack(side=LEFT)
        Button(col4,text="=",width=8,height=3,command=self.sum).pack(side=LEFT)
        
        col4 = Frame();col4.pack()
        Button(col4,text="C",width=8,height=3,command=lambda:self.text.delete(1.0,END)).pack(side=LEFT)
    
    def add(self,num:str):
        self.text.insert(END,num)
        
    def sum(self):
        text = self.text.get(0.0,END)
        try:
            total = str(eval(text))
            self.text.delete(1.0,END)
            self.text.insert(END,total)
        except:
            self.text.delete(1.0,END)
            self.text.insert(END,"Error")
        
if __name__ == "__main__":
    app = gui()
    app.title("Calculator")
    app.mainloop()