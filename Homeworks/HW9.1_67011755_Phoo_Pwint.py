from tkinter import *

class Phone:
    def init(self):
        window = Tk()
        window.title("KMITL Phone")

        f1 = Frame(window)
        f1.pack()

        self.numbers = ""
        self.box = Label(f1, text=self.numbers)
        self.box.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        f2 = Frame(window)
        f2.pack()

        one = Button(f2, text="1", width=10, height=3, command=lambda: self.pressingButton("1"))
        one.grid(row=0, column=0, padx=3, pady=3)

        two = Button(f2, text="2", width=10, height=3, command=lambda: self.pressingButton("2"))
        two.grid(row=0, column=1, padx=3, pady=3)

        three = Button(f2, text="3", width=10, height=3, command=lambda: self.pressingButton("3"))
        three.grid(row=0, column=2, padx=3, pady=3)

        four = Button(f2, text="4", width=10, height=3, command=lambda: self.pressingButton("4"))
        four.grid(row=1, column=0, padx=3, pady=3)

        five = Button(f2, text="5", width=10, height=3, command=lambda: self.pressingButton("5"))
        five.grid(row=1, column=1, padx=3, pady=3)

        six = Button(f2, text="6", width=10, height=3, command=lambda: self.pressingButton("6"))
        six.grid(row=1, column=2, padx=3, pady=3)

        seven = Button(f2, text="7", width=10, height=3, command=lambda: self.pressingButton("7"))
        seven.grid(row=2, column=0, padx=3, pady=3)

        eight = Button(f2, text="8", width=10, height=3, command=lambda: self.pressingButton("8"))
        eight.grid(row=2, column=1, padx=3, pady=3)

        nine = Button(f2, text="9", width=10, height=3, command=lambda: self.pressingButton("9"))
        nine.grid(row=2, column=2, padx=3, pady=3)

        star = Button(f2, text="*", width=10, height=3, command=lambda: self.pressingButton("*"))
        star.grid(row=3, column=0, padx=3, pady=3)

        zero = Button(f2, text="0", width=10, height=3, command=lambda: self.pressingButton("0"))
        zero.grid(row=3, column=1, padx=3, pady=3)

        hash_btn = Button(f2, text="#", width=10, height=3, command=lambda: self.pressingButton("#"))
        hash_btn.grid(row=3, column=2, padx=3, pady=3)
        f3=Frame(window)
        f3.pack()
        talk = Button(f3, text="TALK", width=16, height=3, command=lambda: self.pressingButton("talk"))
        talk.grid(row=4, column=0, padx=3, pady=3)

        back = Button(f3, text="<", width=16, height=3, command=lambda: self.pressingButton("<"))
        back.grid(row=4, column=1, padx=3, pady=3)

        window.mainloop()

    def pressingButton(self, button):
        if button == "<":
            if len(self.numbers) <= 1:
                self.numbers = ""
            else:
                self.numbers = self.numbers[:-1]
            self.box["text"] = self.numbers
        elif button == "talk":
            dialog = Toplevel()
            dialog.title("Talk")
            Label(dialog, text="Dialing " + self.numbers).pack()
        else:
            self.numbers += button
            self.box["text"] = self.numbers

Phone()
