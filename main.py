from tkinter import *
from tkinter import filedialog
import Image



class Window:
    def __init__(self):
        window = Tk()
        window.geometry("1285x650")
        window.title("Photo Designer")
        self.title = Label(window, text='~Photo Designer~', fg="pink", pady=10, width=30, font=("Chiller", 50))
        self.choseImage = Button(window, text='Chose Image📸', activebackground="lightgray", pady=10, width=20,
                                 font=("Chiller", 30), command=self.choseImage)
        self.cutImage = Button(window, text='Cut Image✂', activebackground="lightgray", pady=10, width=15,
                               font=("Chiller", 30), command=self.cutImage)
        self.drowShape = Button(window, text='Drow Shape🖌', activebackground="lightgray", pady=10, width=15,
                                font=("Chiller", 30), command=self.drowShape)
        self.addText = Button(window, text='Add Text🖍', activebackground="lightgray", pady=10, width=15,
                              font=("Chiller", 30), command=self.get_text)
        self.saveImage = Button(window, text='Save Image📥', activebackground="lightgray", pady=10, width=15,
                                font=("Chiller", 30), command=self.save_image)
        self.moreDesign = Button(window, text='More Designs', activebackground="lightgray", pady=10, width=15,
                                 font=("Chiller", 30), command=self.more_designs)
        self.exit = Button(window, text='Exit❌', activebackground="lightgray", pady=10, width=11, font=("Chiller", 20),
                           command=window.quit)
        self.img = None
        self.path = None
        self.text = None
        self.select = None
        self.designs_window = None
        self.shape_window = None
        self.txt_input = None
        self.position()
        window.mainloop()

    def position(self):
        self.title.grid(row=0, column=1, pady=10, padx=10)
        self.exit.grid(row=1, column=2, pady=10, padx=10)
        self.choseImage.grid(row=2, column=1, pady=10, padx=10)
        self.cutImage.grid(row=3, column=0, pady=10, padx=10)
        self.addText.grid(row=3, column=2, pady=10, padx=10)
        self.drowShape.grid(row=4, column=0, pady=10, padx=10)
        self.saveImage.grid(row=4, column=2, pady=10, padx=10)
        self.moreDesign.grid(row=4, column=1, pady=10, padx=10)

    def choseImage(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.path = file_path
            self.img = Image.image("image", file_path)

    def cutImage(self):
        if self.path:
            self.img.set_action("cut")

    def addText(self):
        self.img.set_txt(self.text)
        self.img.set_action("txt")

    def get_text(self):
        text_window = Tk()
        text_window.geometry("500x250")
        text_window.title("Enter txt")

        def on_submit():
            self.text = text_entry.get("1.0", "end-1c")
            text_window.destroy()

        text_entry = Text(text_window, height=5, width=30)
        text_entry.pack()
        submit_button = Button(text_window, text="Submit📩", activebackground="lightgray", pady=8, width=15,
                               font=("Chiller", 25), command=on_submit)
        submit_button.pack()
        self.addText()
        text_window.mainloop()



    def drowShape(self):
        self.shape_window = Toplevel()
        self.shape_window.geometry("450x300")
        self.shape_window.title("Chose shape")
        self.shape_window.title = Label(self.shape_window, text='~Chose Shape~', fg="pink", pady=8, width=10,
                                   font=("Chiller", 30))
        self.shape_window.line = Button(self.shape_window, text='Line➖', activebackground="lightgray", pady=8, width=14,
                                   font=("Chiller", 15), command=self.add_line)
        self.shape_window.circle = Button(self.shape_window, text='circle⭕', activebackground="lightgray", pady=8, width=14,
                                     font=("Chiller", 15), command=self.add_circle)
        self.shape_window.rectangle = Button(self.shape_window, text='Rectangle🟥', activebackground="lightgray", pady=8, width=14,
                                        font=("Chiller", 15), command=self.add_rectangle)

        self.shape_window.title.grid(row=0, column=0, pady=10, padx=10)
        self.shape_window.line.grid(row=1, column=1, pady=10, padx=10)
        self.shape_window.circle.grid(row=1, column=2, pady=10, padx=10)
        self.shape_window.rectangle.grid(row=2, column=1, pady=10, padx=10)
        self.shape_window.mainloop()

    def add_line(self):
        self.img.set_action("add_line")
        self.shape_window.destroy()

    def add_circle(self):
        self.img.set_action("add_circle")
        self.shape_window.destroy()

    def add_rectangle(self):
        self.img.set_action("add_rectangle")
        self.shape_window.destroy()

    def save_image(self):
        filename = filedialog.asksaveasfilename(defaultextension=".jpg",
                                                   title="בחר מיקום לשמירה")
        # בדיקה אם המשתמש בחר מיקום
        if filename:
            self.img.set_filename(filename)

    def more_designs(self):
        self.designs_window = Toplevel()
        self.designs_window.geometry("430x400")
        self.designs_window.title("More Designs")
        self.designs_window.title = Label(self.designs_window, text='~ More designs ~', fg="pink", pady=8, width=10,
                                     font=("Chiller", 30))
        self.designs_window.right = Button(self.designs_window, text='Turn right →', activebackground="lightgray", pady=8, width=14,
                                      font=("Chiller", 15), command=self.right)
        self.designs_window.left = Button(self.designs_window, text='Turn left ←', activebackground="lightgray", pady=8, width=14,
                                     font=("Chiller", 15), command=self.left)
        self.designs_window.Invert = Button(self.designs_window, text='Invert image 🔃', activebackground="lightgray", pady=8,
                                       width=14,
                                       font=("Chiller", 15), command=self.Invert)
        self.designs_window.Clean = Button(self.designs_window, text='Clean picture', activebackground="lightgray", pady=8,
                                      width=14,
                                      font=("Chiller", 15), command=self.Clean)
        self.designs_window.frame = Button(self.designs_window, text='Add frame', activebackground="lightgray", pady=8, width=14,
                                      font=("Chiller", 15), command=self.frame)
        self.designs_window.title.grid(row=0, column=1, pady=10, padx=10)
        self.designs_window.right.grid(row=1, column=0, pady=10, padx=10)
        self.designs_window.left.grid(row=1, column=2, pady=10, padx=10)
        self.designs_window.Invert.grid(row=2, column=1, pady=10, padx=10)
        self.designs_window.Clean.grid(row=3, column=0, pady=10, padx=10)
        self.designs_window.frame.grid(row=3, column=2, pady=10, padx=10)
    def frame(self):
        self.img.set_action("add_frame")
        self.designs_window.destroy()
    def Clean(self):
        self.img.set_action("first_image")
        self.designs_window.destroy()

    def Invert(self):
        self.img.set_direction(1)
        self.designs_window.destroy()

    def left(self):
        self.img.set_direction(-2)
        self.designs_window.destroy()

    def right(self):
        self.img.set_direction(-1)
        self.designs_window.destroy()

image = Window()
