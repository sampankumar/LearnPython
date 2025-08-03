import tkinter

window = tkinter.Tk()
button = tkinter.Button(window, text="Hi, please don't press this button", width=30)
button.pack(padx=10,pady=10)
clickcount = 0
def onClick(event):
    global clickcount
    clickcount = clickcount + 1
    if clickcount == 1:
        button.configure(text="Don't. Press. The. Button!")
    elif clickcount == 2:
        button.configure(text="Next time you click it, I'll take it away!")
    else:
        button.pack_forget()
button.bind("<ButtonRelease-1>", onClick)
window.mainloop()
