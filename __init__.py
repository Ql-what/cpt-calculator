from tkinter import *
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
        self.hi = None
    def initWidgets(self):
        self.show = Label(relief= SUNKEN, font = ('Courier New', 24),\
         width=23, bg='white', anchor=W)
        self.show.pack(side=TOP, pady=10)
        p = Frame(self.master)
        p.pack(side=TOP)
        names = ("+", "1" , "2" , "3" , "return"
         ,"-", "4" , "5" , "6" , "**" , "*", "7" , "8"
         , "9", "//", "/" , "." , "0" , "%", "=")
        for i in range(len(names)):
         b = Button( p , text=names[i], font=('Verdana', 20), width=5)
         b.grid(row=i // 5, column=i % 5)
         b.bind('<Button-1>', self.click)
         if b['text'] == 'return': b.bind('<Button-1>', self.clean)

        self.i = 0

    def click(self, event):
        if(event.widget['text'] in ('0', '1', '2', '3',\
        '4', '5', '6', '7', '8', '9', '.')):
            if self.i == 0:
                self.show['text']= ''
                self.show['text'] = self.show['text'] + event.widget['text']
                self.i = self.i + 1
                print(self.i)
            else:
                self.show['text'] = self.show['text'] + event.widget['text']
                self.i= self.i + 1
                print(self.i)

        elif(event.widget['text'] in ('+', '-', '*', '/', '%', '**', '//')):
            self.show['text'] = self.show['text'] + event.widget['text']
        elif(event.widget['text']=='=' and self.show['text'] is not None):
            self.hi = self.show['text']
            self.show['text'] = str(eval(self.hi))
            print(self.hi)
            self.show['text'] = str(eval(self.hi))
            self.hi = None
            self.i = 0

    def clean(self, event):
        self.hi = None
        self.show['text'] = ''
root= Tk()
root.title("calculater")
App(root)
root.mainloop()
