from tkinter import *

root = Tk()
root.configure(bg="pale green")
root.title("Account Register")
root.geometry("1600x1600")

LabelName = Label(root, text="User Name:", bg="pale green", font=("Arial", 35))
LabelEmail = Label(root, text="Email:", bg="pale green", font=("Arial", 35))

EntryName = Entry(root, font=("Arial", 35))
EntryEmail = Entry(root, font=("Arial", 35))

LabelName.place(anchor=CENTER, relx=0.37, rely=0.1)
LabelEmail.place(anchor=CENTER, relx=0.39, rely=0.3)

EntryName.place(anchor=CENTER, relx=0.63, rely=0.1)
EntryEmail.place(anchor=CENTER, relx=0.61, rely=0.3)

LabelDictionary = Label(root, bg="pale green", font=("Arial", 35))
LabelDictionary.place(anchor=CENTER, relx=0.5, rely=0.7)

Dictionary = {}


class AddUser:
    def add_user(self, name, email):
        Dictionary[name] = email
        LabelDictionary["text"] = Dictionary


User1 = AddUser()

AddBtn = Button(
    root,
    text="Add User",
    bg="pale turquoise",
    font=("Arial", 35),
    command=lambda: User1.add_user(EntryName.get(), EntryEmail.get()),
)
AddBtn.place(anchor=CENTER, relx=0.5, rely=0.5)

root.mainloop()
