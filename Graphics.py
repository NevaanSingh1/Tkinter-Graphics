from tkinter import *
window = Tk()
window.title("Tkiinter Sample Window")
window.geometry("800x800")

greetings = Label(text="Hello User", fg="#3e82c2", bg="#34ebeb")
button = Button(text="Click Me", fg="#B8AC2A", bg="#1B11CA")
entry = Entry(fg="#FF5733", bg="#C70039")
greetings.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief = RAISED, borderwidth=5)
frame.pack()
label = Label(master=frame, text="Sample Frame")
label.pack()
textbox = Text(fg = "Green", bg="Black")
textbox.pack()

window.mainloop()