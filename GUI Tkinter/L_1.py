from tkinter import *
window = Tk() # create windows
window.title('Window')
window.geometry('500x300') # windows size

label = Label(window, text="Some label", font='Arial 16')
label.pack(side = TOP)

label_1 = Label(window, text="Some text", font=('Arial', 24, 'bold'))

label_1.pack(padx=150, pady=50)
window.mainloop()