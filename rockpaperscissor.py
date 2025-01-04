from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination calculator")
root.geometry("600x600")

upload = Image.open("money.webp")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)

label = Label(root, bg="blue", image=image)
label.place(x=180, y=20)
label1 = Label(root, bg="green", text="Welcome to the denomination caluclator")

def msg():
    msgbox = messagebox.showinfo("Alert", "Do you want to proceed to denomination counter?")
    if msgbox == "ok":
        topwin()
    
button = Button(root, text="Let's get started", command=msg, bg="blue")
button.place(x=260, y=360)
label1.place(x=180, y=340)

def topwin():
    top = Toplevel()
    top.title("Denomination calculator")
    top.configure(bg='light grey')
    top.geometry("600x350+50+50")

    label2 = Label(top, text="Enter total amount", bg='light grey')
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination", bg='light grey')

    l1 = Label(top, text="50", bg='light grey')
    l2 = Label(top, text="20", bg='light grey')
    l3 = Label(top, text="10", bg='light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    
    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note50 = amount // 50
            amount %= 

root.mainloop()
