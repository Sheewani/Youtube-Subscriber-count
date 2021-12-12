from tkinter import *
from subs_counter import get_sub_count
window = Tk()



Label1 = Label(text ="Youtube Counter", font=("Helvetica", 40))
Label1.pack()
label2 =Label(text="Current Subscribers", font=("Helvetica", 20))
label2.pack()
label3 = Label(text=get_sub_count(), font=("Roboto", 50))
label3.pack()


def update_count():
    label3.config(text=get_sub_count())
    window.after(3000, update_count)
window.after(0,update_count)    


window.mainloop()