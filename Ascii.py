from tkinter import *
root = Tk()
root.geometry("400x400")
root.configure(bg="teal")

ibox = Entry(root)
ibox.place(relx=0.5, rely=0.3, anchor=CENTER)

lbl = Label(root, text="The ASCII values for the name are ", fg="white", bg="teal")
lbl.place(relx=0.5, rely=0.6, anchor=CENTER)

def asciiconverter():
    lbl["text"] = "The ASCII values for the name are "
    word = ibox.get()
    for x in word:
        Ascii = ord(x)
        lbl["text"] += str(Ascii) + " "

btn = Button(root, text="Do you want to know the ASCII for your name?", command=asciiconverter)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()